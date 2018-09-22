

"""
Usage:
    torchbase version [<torch>] [<checkpoint>]
    torchbase run     [options] <torch> <file1> [<file2>...] [--checkpoint=<checkpoint>] [--map=<mapper>]
    torchbase pull    [options] <torch> [--checkpoint=<checkpoint>]
    torchbase convert_pubmlst [options] <new_torch_name> [--description=<description>] <profile_file> <locus_fasta1> [<locus_fasta2>...]
    torchbase update  [options] <torch>

Options:
    -h --help        Show this screen
    -v --verbose     Verbose logging
    
"""


#import avro.schema
import docpie
import reference
import reference.schema
import sys
import logging
from sys import stderr, argv




from functools import wraps

if 'version' not in argv:
	logging.basicConfig(format='%(asctime)s - %(name)s \t- %(levelname)s\t - %(message)s', stream=stderr, level=logging.INFO)
log = logging.getLogger('torchbase')

version = "0.1a"

command_dict = {}
def command(name):
	def command_decorator(func):
		command_dict[name] = func
		return func
	return command_decorator


@command("version")
def get_version(torch=None, checkpoint=None, *a, **k):
	print(f"Torchbase v. {version}")
	if torch:
		tor = reference.TorchFile(torch)
		print(f"{tor.name} v. {tor.version}")

@command("run")
def run(torch, file1, file2=[], *a, **k):
	tor = reference.TorchFile(torch)
	from mapping.mapping import run_srst2
	if file2:
		results = [run_srst2(tor, locus['Name'], file1, file2[0] for locus in tor.reference['loci']]
	else:
		results = [run_srst2(tor, locus['Name'], file1 for locus in tor.reference['loci']]

@command("pull")
def pull(torch, *a, **k):
	pass

@command("convert_pubmlst")
def convert(new_torch_name, profile_file, locus_fasta1, locus_fasta2=None, description="", *a, **k):
	from convert.main import convert_pubmlst as c_convert
	loci_fasta = (locus_fasta2 or [])
	loci_fasta.insert(0, locus_fasta1)
	return c_convert(new_torch_name, profile_file, loci_fasta, description)

@command("update")
def update(torch, *a, **k):
	pass

def main():
	pie = docpie.Docpie(doc=__doc__, version=None, name="torchbase", appearedonly=True)
	#pie.preview()
	args = pie.docpie()
	args = {k.replace('>','').replace('<',''):v for k,v in args.items()}
	[log.info(f"{k}:{v}") for k,v in args.items() if v]
	for key, command in command_dict.items():
		if args.get(key):
			log.debug(key)
			exit(command_dict[key](**args))
	print(f"Torchbase v. {version}")
	print("High-performance typing schemes")
	print(__doc__)

if __name__ == '__main__':
	main()
	
