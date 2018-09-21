#from torchbase import schema
from torchbase import version
from torchbase.reference.schema import Schema, Reference, Types, Locus, Variant, Allele, Presence 

import csv
import tempfile
import ipfsapi
from os.path import join, basename, dirname
from shutil import make_archive
from hashlib import sha256 as hasher
import logging

log = logging.Logger('torchbase.reference')

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


def convert_fasta(new_package_name, profile_file, loci_files=[], description=""):
	log = log.getChild('covert_fasta')
	loci = []
	types = []
	for loci_file in loci_files:
		log.info(f"Opening {loci_file}...")
		alleles = []
		with open(loci_file, 'r') as loci_file_f:
			for name, seq, _ in readfq(loci_file_f):
				hash_ = hasher(seq).hexdigest()[:10]
				log.info(f"{name}: {hash_}")
				alleles.append(Allele(name=name, hash=hash_))
		loci.append(Locus(name=basename(loci_file).split('.')[0]), alleles=alleles)
	with open(profile_file, 'r') as profile_f:
		rdr = csv.reader(profile_f, delimiter='\t')
		header = rdr.next()
		log.debug(header)
		for row in rdr:
			pass #do stuff
	#some types stuff
	reference = Reference(name=new_package_name, version="1.0.0", types=types, loci=loci)
	def allele_generator():
		for loci_file in loci_files:
			with open(loci_file, r) as loci:
				for _, seq, _ in readfq(loci):
					yield seq
	return Schema(reference=reference), allele_generator()
	


def build_database(type_definition_struct, alleles=[], config_file_name='config.json', data_file_name='sequences.dat', delete=False):
	"construct a typing scheme package from the type definition in our schema and an iterator over alleles"
	log = log.getChild('build_db')
	with tempfile.TemporaryDirectory(prefix=f"torchbase_{version.replace('.','_')}", delete=delete) as temp_package:
		with open(join(temp_package, config_file_name), 'w') as config:
			#avro marshall config >> config.json
		with open(join(temp_package, data_file_name), 'w') as data:
			data.writelines(alleles)
		output_file = tempfile.NamedTemporaryFile().name
		make_archive(basename(output_file), format="gztar", root_dir=dirname(output_file), base_dir=temp_package)
		return output_file



def register_database(new_package_name, path_to_package):
	log = log.getChild('register_db')
	#api = ipfsapi.connect('127.0.0.1', 5001) #need to abstract this later
	#record = api.add(path_to_archive) #hash of directory
