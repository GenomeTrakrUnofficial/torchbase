# Test files for MLST typing

These are minimal fasta files for testing out typing using regular MLST, using the [Salmonella enterica](https://pubmlst.org/data/) scheme available on PubMLST. These consist of concatenated alleles linked together by `aaa`, which I found was required when testing out typing from reads with **SRST2** (otherwise too few reads map to edges).

## 1. Normal case

File: `senterica-st4-normal.fasta`. Should give ST 1.

## 2. Overlapping allele case

File: `senterica-st1-overlap-genes.fasta`. Dervied from ST 4, of which the allele for thrA is type 5, but thrA type 783 is a subsequence of allele 5. This is reported by the software [mlst](https://github.com/tseemann/mlst) software as `thrA(5,783)`, though SRST2 reports it correctly as variant 5. So could be useful for a test.

# Simulated reads

To simulate reads for testing read/mapping-based typing, you can run something like:

```
art_illumina -ss MSv1 -i senterica-st4-normal.fasta -l 150 -f 20 -o senterica-st4-normal
```

I found I had to use a coverage of 20 to get **SRST2** to properly type.
