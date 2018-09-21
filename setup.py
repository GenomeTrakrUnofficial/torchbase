from setuptools import setup
from torchbase.torchbase import version

setup(
	name="torchbase",
	version=version,
	description="High-performance typing schemes",
	author="Torchbase Hackathon Group",
	author_email="justin.payne@fda.hhs.gov",
	license='CC0 1.0',
	classifiers=[
		'Development Status :: 3 - Alpha',
		'Environment :: Console',
		'Intended Audience :: Science/Research',
		'License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',
		'Topic :: Utilities'
	],
	packages=['torchbase'],
	package_data={'reference.schema':['reference/schema/*avdl', 'reference/schema/*avsc', 'reference/schema/*avpr']},
	url="https://github.com/GenomeTrakrUnofficial/torchbase",
	entry_points=dict(
		console_scripts=['torchbase = torchbase.torchbase.main']
	),
)