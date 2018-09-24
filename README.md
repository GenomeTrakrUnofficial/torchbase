# Torchbase
Python framework for microbial typing by reference

## Description
Torchbase is an attempt to unify the 'work' of writing microbial
sequence typing pieplines. Many forms of sequence typing are
contemplated - MLST, wg/cgMLST AMR prediction, and others.

Additionally, Torchbase will have transparent versioning and
distribution of typing reference/profiling packages ('torches')
to aid reproducible research and consistent typing results.

## Usage

		torchbase version [<torch>] [<checkpoint>]
		torchbase run     [options] <torch> <file1> [<file2>...] [--checkpoint=<checkpoint>] [--map=<mapper>]
		torchbase pull    [options] <torch> [--checkpoint=<checkpoint>]
		torchbase convert_pubmlst [options] <new_torch_name> [--description=<description>] <profile_file> <locus_fasta1> [<locus_fasta2>...]
		torchbase update  [options] <torch>

	Options:
		-h --help        Show this screen
		-v --verbose     Verbose logging
    

## Goals
Consistent reference format  
IPFS-based reference distribution  
Modular allele detection?  
Alignment parameter tuning in reference package  
Parameter override in runtime  
Typing:  
	Antigen-based   
	wgMLST?  
	Other stuff?  
	2-stage approaches - alignment, then SNP calling  
Stuff in the reference package:  
	Allele references  
	Allelic profile table  
	Parameters for alignment and SNP calling  
	Workflow description (stages, data flow)  
Cool name  
Genes that don't map, alleles that map twice, other weirdo cases

Front-end the back-end we want people to use

## Mind map
https://www.mindmeister.com/1150608310?t=Dcfo0Hpx04


### To generate avpr file (for devs)

- Download java
- Download avrotools.jar
- java -jar avro-tools-1.8.2.jar idl torchbase/reference/schema/torchbase.avdl

### To create schema_classes.py (for devs)

- install avrogen python package
```
from avrogen import write_protocol_files
write_protocol_files(string_of_avpr_file, output_dir)
```

### Requirements

The following programs are required to run srst2 to get the allele calls and must be available in PATH
- bowtie2 v2.1.0 http://bowtie-bio.sourceforge.net/bowtie2/index.shtml
- SAMtools v0.1.18 https://sourceforge.net/projects/samtools/files/samtools/0.1.18/