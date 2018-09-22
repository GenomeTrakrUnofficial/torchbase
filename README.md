# Torchbase
Python framework for microbial typing by reference

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


### To generate avpr file

- Download java
- Download avrotools.jar
- java -jar avro-tools-1.8.2.jar idl torchbase/reference/schema/torchbase.avdl

### To create schema_classes.py

- install avrogen python package
```
from avrogen import write_protocol_files
write_protocol_files(string_of_avpr_file, output_dir)
```

### Requirements

The following programs are required to run srst2 to get the allele calls and must be available in PATH
- bowtie2 v2.1.0 http://bowtie-bio.sourceforge.net/bowtie2/index.shtml
- SAMtools v0.1.18 https://sourceforge.net/projects/samtools/files/samtools/0.1.18/