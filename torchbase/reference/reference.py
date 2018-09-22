from contextlib import contextmanager
import tarfile
import tempfile
import json
from hashlib import sha256 as hasher
#
# from schema import *
			
				
class Torch(object):

	def __init__(self, torch_file):
		self.torch_f = tarfile.open(torch_file, 'r|gz')
		self.config, self.data = self.torch_f.getmembers()
		self.config = json.load(self.config)

	@property
	def hash_index(self):
		if hasattr(self, '_hash_index'):
			return self._hash_index
		self._hash_index = self.index_data()
		return self._hash_index

	@property
	def reference(self):
		return self.config['reference']

	@property
	def name(self):
		return self.config['Name']

	@property
	def version(self):
		return self.config['Version']

	@property
	def description(self):
		return self.config['Description']

	def alleles_from_locus(self, locus):
		for locus_name, alleles in self.config['reference']['loci']:
			if locus_name == locus:
				return alleles

	def index_data(self):
		hash_index = {}
		for seq in data.readlines():
			hashh = hasher(seq.encode('utf-8')).hexdigest()[:10]
			self.hash_index[hashh] = data.tell()
		self.data.seek(0)
		return hash_index

	@contextmanager
	def expose_torch_as_fasta(self, locus):
		with tempfile.NamedTemporaryFile(prefix=torch.split('_')[-1]) as temp_fasta:
			for allele in self.alleles_from_locus:
				name = allele['Name']
				hashh = allele['Hash']
				data.seek(self.hash_index[hashh])
				temp_fasta.write(f"> {hashh}\n")
				b = data.read(1)
				while True:
					temp_fasta.write(b)
					if b = '\n':
						break
					b = data.read(1)
			temp_fasta.flush()
			yield temp_fasta.name