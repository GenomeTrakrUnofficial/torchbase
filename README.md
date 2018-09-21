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


### To generate avsc file

- Download java
- Download avrotools.jar
- java -jar avro-tools-1.8.2.jar idl torchbase/reference/schema/torchbase.avdl