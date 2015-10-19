# Methods:
* Clean the IonTorrent reads by removing indexes (barcodes) from our reads and
  dropping sequences shorter than 21 base pairs.
  
## Assembly using MITObim
Used the IONTOR_SETTINGS in the ``manifest.conf`` file that was used by ``mira``,
which is a sequence assembler and sequence mapping for sequencing data (including
IonTorrent).
The flag ``--iontor`` was used in the MITObim command line to do the mapping of the
assembled sequence to the reference genome of a related taxon.

* Used *Libythea celtis* mitochondrial genome (NCBI Reference Sequence: NC_016724.1)
  as reference for assembly using MITObim.

./MITObim_1.8.pl --iontor -start 1 -end 10 -sample testpool -ref libythea_mito_genome.fa -readpool read_without_indexes.fastq -maf libytheana_d_results/libytheana_out.maf > log

## Annotation
http://onlinelibrary.wiley.com/enhanced/doi/10.1111/syen.12071/

* Find identifying tRNA genes, usually via secondary structure covariation models

Annotation using MITOS http://mitos.bioinf.uni-leipzig.de/

Annotated genes in Libytheana assembly. Spurious genes have been removed as they
have low scores. Some duplicates are explained as split genes (we couldnt get
the full sequence and they appear in two pieces).


| seq                               | start | end   | gene       | score       |   |
|-----------------------------------|-------|-------|------------|-------------|---|
| Libytheana_assembly_iontor_iontor | 172   | 240   | trnM(cat)  | 1.012e-10   | + |
| Libytheana_assembly_iontor_iontor | 240   | 306   | trnI(gat)  | 1.915e-10   | + |
| Libytheana_assembly_iontor_iontor | 303   | 372   | trnQ(ttg)  | 5.751e-09   | - |
| Libytheana_assembly_iontor_iontor | 449   | 662   | nad2-0_a   | 3271235.1   | + |
| Libytheana_assembly_iontor_iontor | 899   | 983   | nad2-0_b   | 716897.7    | + |
| Libytheana_assembly_iontor_iontor | 1433  | 1500  | trnW(tca)  | 1.946e-10   | + |
| Libytheana_assembly_iontor_iontor | 1492  | 1555  | trnC(gca)  | 6.693e-10   | - |
| Libytheana_assembly_iontor_iontor | 1562  | 1629  | trnY(gta)  | 3.803e-09   | - |
| Libytheana_assembly_iontor_iontor | 1639  | 3148  | cox1       | 286864431.6 | + |
| Libytheana_assembly_iontor_iontor | 3167  | 3234  | trnL2(taa) | 3.606e-10   | + |
| Libytheana_assembly_iontor_iontor | 3234  | 3900  | cox2       | 104494061.7 | + |
| Libytheana_assembly_iontor_iontor | 3916  | 3987  | trnK(ctt)  | 4.069e-08   | + |
| Libytheana_assembly_iontor_iontor | 3989  | 4057  | trnD(gtc)  | 9.551e-08   | + |
| Libytheana_assembly_iontor_iontor | 4057  | 4225  | atp8       | 78329.5     | + |
| Libytheana_assembly_iontor_iontor | 4224  | 4890  | atp6       | 47018338.8  | + |
| Libytheana_assembly_iontor_iontor | 4931  | 5684  | cox3       | 169421514.4 | + |
| Libytheana_assembly_iontor_iontor | 5689  | 5739  | trnG(tcc)  | 0.0002665   | + |
| Libytheana_assembly_iontor_iontor | 5795  | 6101  | nad3       | 12312230.5  | + |
| Libytheana_assembly_iontor_iontor | 6114  | 6182  | trnA(tgc)  | 0.0001019   | + |
| Libytheana_assembly_iontor_iontor | 6189  | 6242  | trnR(tcg)  | 0.0002755   | + |
| Libytheana_assembly_iontor_iontor | 6249  | 6316  | trnN(gtt)  | 1.03e-07    | + |
| Libytheana_assembly_iontor_iontor | 6314  | 6375  | trnS1(gct) | 1.319e-07   | + |
| Libytheana_assembly_iontor_iontor | 6376  | 6443  | trnE(ttc)  | 0.0001674   | + |
| Libytheana_assembly_iontor_iontor | 6600  | 7056  | nad5-1     | 7952978.5   | - |
| Libytheana_assembly_iontor_iontor | 7069  | 8140  | nad5-0     | 176312768.9 | - |
| Libytheana_assembly_iontor_iontor | 8241  | 8305  | trnH(gtg)  | 3.565e-07   | - |
| Libytheana_assembly_iontor_iontor | 8309  | 9095  | nad4_b     | 114240489.3 | - |
| Libytheana_assembly_iontor_iontor | 9162  | 9351  | nad4_a     | 22414769.2  | - |
| Libytheana_assembly_iontor_iontor | 9645  | 9753  | nad4l      | 1149872.8   | - |
| Libytheana_assembly_iontor_iontor | 9936  | 10001 | trnT(tgt)  | 1.018e-07   | + |
| Libytheana_assembly_iontor_iontor | 10001 | 10066 | trnP(tgg)  | 3.272e-09   | - |
| Libytheana_assembly_iontor_iontor | 10079 | 10364 | nad6_a     | 1590693.5   | + |
| Libytheana_assembly_iontor_iontor | 10330 | 10588 | nad6_b     | 538369.8    | + |
| Libytheana_assembly_iontor_iontor | 10622 | 10886 | cob_a      | 55349244.3  | + |
| Libytheana_assembly_iontor_iontor | 10878 | 11724 | cob_b      | 218499514.4 | + |
| Libytheana_assembly_iontor_iontor | 11749 | 11816 | trnS2(tga) | 6.242e-06   | + |
| Libytheana_assembly_iontor_iontor | 11895 | 12705 | nad1       | 130269875.7 | - |
| Libytheana_assembly_iontor_iontor | 12806 | 14166 | rrnL       | 2.1e-09     | - |
| Libytheana_assembly_iontor_iontor | 14168 | 14236 | trnV(tac)  | 4.667e-08   | - |
| Libytheana_assembly_iontor_iontor | 14236 | 15024 | rrnS       | 2.737e-12   | - |


# Analysis

Partitionfinder by gene by codon. See what happens.