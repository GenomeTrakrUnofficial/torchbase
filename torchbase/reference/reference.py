from contextlib import contextmanager
import tarfile
import tempfile
import json
from hashlib import sha256 as hasher
import logging
#
# from schema import *
			
				
class TorchFile(object):

	log = logging.getLogger('torchbase.Torch')

	def __init__(self, torch_file):
		self.torch_f = tor = tarfile.open(torch_file, 'r:gz')
		self.config, self.data = tor.getmembers()
		self.config = json.load(tor.extractfile(self.config))
		self.data = tor.extractfile(self.data)

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
		for loc in self.config['reference']['loci']:
			if loc['Name'] == locus:
				return loc['alleles']
		raise ValueError(f"locus '{locus}' not in reference.")

	def index_data(self):
		hash_index = {}
		beginning = self.data.tell()
		for seq in self.data:
			hashh = hasher(seq.strip()).hexdigest()[:10]
			hash_index[hashh] = beginning
			beginning = self.data.tell()
		self.data.seek(0)
		return hash_index

	def allele_sequences_in_locus(self, locus):
		for allele in self.alleles_from_locus(locus):
				name = allele['Name']
				hashh = allele['Hash']
				self.data.seek(self.hash_index[hashh])
				yield f"> {hashh}\n"
				yield self.data.readline()

	@contextmanager
	def expose_torch_as_fasta(self, locus):
		with tempfile.NamedTemporaryFile(prefix=self.name) as temp_fasta:
			temp_fasta.write(self.allele_sequences_in_locus(locus))
			temp_fasta.flush()
			yield temp_fasta.name


if __name__ == '__main__':
	t = TorchFile('./torchbase_0_1a_bun9qfkj_kudoas.torch')
	print(t.name)
	print(t.version)
	print(t.index_data())
	print(list(t.allele_sequences_in_locus('rnl')))