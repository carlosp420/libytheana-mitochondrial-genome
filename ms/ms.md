# Materials and methods

## Library preparation and IonTorrent sequencing

A MALE/FEMALE specimen of *Libytheana motya* collected in Playa Larga, Cuba  
on April 12, 1968 was used for DNA extraction. The specimen had been
conserved dry in a paper envelope and is currently located in the Wahlberg
collection at Lund University, Lund, Sweden.

The whole thorax was used for DNA extraction using a modified version of the 
Salt-extraction method from @aljanabi1997.
Inspection on a electrophoresis gel suggested that the extracted DNA was 
degraded in some degree, thus it was not sheared previous to library preparation
for Next Generation Sequencing.
We adapted the protocol by @meyer2010 of library preparation for the 
Ion Personal Genome Machine (PGM) sequencer (Ion Torrent, Life Technologies).
In brief, we blunt-end repaired the extracted genomic DNA in order to ligate
the Ion Torrent sequencing adapters A (which included a 10 base pair oligonucleotide
as index or barcode) and P1.
The ligated adapters were filled-in with nucleotides followed by an
amplification step using the forward A adaptor and the reverse P1 adaptor as
primers.
The resulting library was size-selected for around 400 nucleotides in length
by cutting from an electrophoresis gel and sequenced in the Ion Torrent PGM 
on a 318 chip after quality inspection using the 2100 Bioanalyzer (Agilent
Technologies). 

## Sequence assembly
We used a Python script to clean the sequenced Ion Torrent reads by removing
the indexes (barcodes) from our reads and dropping sequences shorter than 21
base pairs.
We used MIRABAIT 4.0.2 (@chevreux1999) to remove reads consisting of sequence
adapters.
We use the software mitochondrial baiting and iterative mapping (MITObim v1.8,
@hahn2013) to assemble the mitochondrial genome of *Libytheana motya*  using 
the mitogenome of *Libythea celtis* (NCBI Reference Sequence: NC_016724.1)
as reference.
We used the IONTOR_SETTINGS in the ``manifest.conf`` file that was employed by
MIRA (including IonTorrent).
The flag ``--iontor`` was used in the MITObim command line to execute the
mapping of the assembled sequence to the reference genome of a related taxon.

We aligned the assembled genome of *Libytheana* against the reference genome of
*Libythea celtis* using MAFFT [@katoh2013] and found a segment of 175 nucleotides
at the start of the N-terminus that could not be aligned. We used BLASTN [@camacho2009]
to test if this fragment actually matches the C-terminus of the reference genome.
We found that it could not be aligned to any end so we manually removed this fragment
from the assembled genome of *Libytheana*.

## Annotation
We used the MITOS web server [@bernt2013] to annotate the assembled mitogenome 
sequence. We used the invertebrate genetic code as parameter for MITOS.

## Assembly quality assessment
We used bowtie 2.2.6 to align our reads to the assembled mitogenome using the
pipeline in Supp Mat 01 (Makefile: make analysis).

Average coverage was measured using samtools and the total length of our assembled
genome:

    > samtools depth cleaned_seqs_bowtie_sorted.bam | awk '{sum +=$3} END {print "Average = ", sum/15227}'
    
Average coverage is 10.38

We used Python and the library pygal v2.0.0 to generate a histogram of the coverage at each base
position.

# Results
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


# Commands
mirabait adapter_sequences.fas CarlosJul2015/CarlosJul2015.fastq baited_seqs
./MITObim_1.8.pl --iontor -start 1 -end 10 -sample testpool -ref libythea_mito_genome.fa -readpool read_without_indexes.fastq -maf libytheana_d_results/libytheana_out.maf > log

# Bibliography
