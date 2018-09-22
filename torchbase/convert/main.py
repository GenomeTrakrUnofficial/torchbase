#from torchbase import schema
from avro import datafile, io
from collections import defaultdict, OrderedDict
from reference.schema import TorchModel, Reference, Types, Locus, Variant, Allele, ProfileElement 
#from reference.schema import SCHEMA as torchbase_schema
from torchbase import version


import csv
import tempfile
import ipfsapi
from os.path import join, basename, dirname, split
#from shutil import make_archive
import tarfile
from hashlib import sha256 as hasher
import logging
import json

logg = logging.Logger('torchbase.reference')

#Heng Li's FASTQ/A reader
#https://github.com/lh3/readfq/blob/master/readfq.py

def readfq(fp): # this is a generator function
    last = None # this is a buffer keeping the last unprocessed line
    while True: # mimic closure; is it a bad idea?
        if not last: # the first record or a record following a fastq
            for l in fp: # search for the start of the next record
                if l[0] in '>@': # fasta/q header line
                    last = l[:-1] # save this line
                    break
        if not last: break
        name, seqs, last = last[1:].partition(" ")[0], [], None
        for l in fp: # read the sequence
            if l[0] in '@+>':
                last = l[:-1]
                break
            seqs.append(l[:-1])
        if not last or last[0] != '+': # this is a fasta record
            yield name, ''.join(seqs), None # yield a fasta record
            if not last: break
        else: # this is a fastq record
            seq, leng, seqs = ''.join(seqs), 0, []
            for l in fp: # read the quality
                seqs.append(l[:-1])
                leng += len(l) - 1
                if leng >= len(seq): # have read enough quality
                    last = None
                    yield name, seq, ''.join(seqs); # yield a fastq record
                    break
            if last: # reach EOF before reading enough quality
                yield name, seq, None # yield a fasta record instead
                break


def convert_pubmlst(new_package_name, profile_file, loci_files=[], description=""):
	"Convert an MLST scheme in PubMLST 'format' into a Torch file and register it in IPFS"
	log = logg.getChild('covert_mlst')
	tor = TorchModel()
	tor.reference = Reference()
	allele_hash_cache = defaultdict(dict)
	# Open allele files, scan and hash alleles, add them to the Torch metadata
	#
	# --JSP
	for loci_file in loci_files:
		log.info(f"Opening {loci_file}...")
		locus_name = basename(loci_file).split('.')[0]
		log.debug(locus_name)
		locus = Locus()
		locus.Name = locus_name
		with open(loci_file, 'r') as loci_file_f:
			for defline, seq, _ in readfq(loci_file_f):
				loc, name = defline.split('_')
				hash_ = hasher(seq.encode('utf-8')).hexdigest()[:10]
				log.info(f"{loc} {name}: {hash_}")

				allele_hash_cache[loc][name] = hash_

				a = Allele()
				a.Name = name
				a.Hash = hash_
				locus.alleles.append(a)
		tor.reference.loci.append(locus)
	# Open the profile definition TXT and link allele names to allele hashes,
	# then add the profile definitions to the Torch struct.
	# --JSP
	profile_cache = defaultdict(dict)
	log.info(f"Opening profile definitions in {profile_file}...")
	with open(profile_file, 'r') as profile_f:
		rdr = csv.reader(profile_f, delimiter='\t')
		header = rdr.__next__()
		log.debug(header)
		for row in rdr:
			st = row[0]
			log.debug(f"ST {st}")
			for loc, allele in zip(header[1:], row[1:]):
				ha = allele_hash_cache[loc][allele]
				profile_cache[st][loc] = ha
				#log.debug(f"{loc}_{allele}/{ha}")
	[log.debug(f"{k}:{v}") for k, v in profile_cache.items()]
	#Create types and add to Types array
	#--JSP
	for type_name, allelic_profile in profile_cache.items():
		t = Types()
		t.Name = type_name
		for locus, hashh in allelic_profile.items():
			p = ProfileElement()
			p.LocusName = locus
			p.AlleleName = hashh
			t.profile.append(p)
		tor.types.append(t)
	#We need to serialize the alleles to a file in the next step, so create and return
	#a generator to access the allele sequence data only, with line delimiters.
	#--JSP
	def allele_generator():
		for loci_file in loci_files:
			with open(loci_file, 'r') as loci:
				for _, seq, _ in readfq(loci):
					yield seq
					yield '\n'
	#Complete the Torch, build the files, register the Torch
	#--JSP
	tor.Name = new_package_name
	tor.Version = '1.0.0'
	tor.Description = description
	return register_torch(new_package_name, build_torch(tor, allele_generator()))
	


def build_torch(type_definition_struct, alleles=[], config_file_name='config.json', data_file_name='sequences.dat', delete=False):
	"construct a typing scheme package from the type definition in our schema and an iterator over alleles"
	log = logg.getChild('build_db')
	log.info(type_definition_struct)
	with tempfile.TemporaryDirectory(prefix=f"torchbase_{version.replace('.','_')}_", suffix=f"_{type_definition_struct.Name}") as temp_package:
		log.info(temp_package)
		with open(join(temp_package, config_file_name), 'w') as config:
			json.dump(type_definition_struct, config, indent=2)
		with open(join(temp_package, data_file_name), 'w') as data:
			data.writelines(alleles)
		#name, ddir = split(tempfile.NamedTemporaryFile(suffix="_torch", delete=delete).name)
		#log.debug(join(ddir, name))
		#archive = make_archive(basename(temp_package), format="gztar", base_dir=temp_package)
		with tarfile.open(f"{basename(temp_package)}.torch", 'w:gz') as archive:
			archive.add(join(temp_package, config_file_name))
			archive.add(join(temp_package, data_file_name))
			log.info(f"New torch created at {archive.name}")
			#input()
			return archive.name



def register_torch(new_package_name, path_to_package):
	log = logg.getChild('register_db')
	#api = ipfsapi.connect('127.0.0.1', 5001) #need to abstract this later
	#record = api.add(path_to_archive) #hash of directory
