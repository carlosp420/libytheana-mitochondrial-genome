# method taken from http://ged.msu.edu/angus/tutorials-2012/bwa_tutorial.html
# Mapping reads with bwa and bowtie
# we will use bowtie2

analysis: cleaned_seqs_bwa.sam cleaned_seqs_bowtie.sam cleaned_seqs_bwa_sorted.bam cleaned_seqs_bowtie_sorted.bam

# copy ref genome to current folder
libytheana_clipped.fasta: /data/projects/libytheana_mito/data/derived/libytheana_clipped.fasta
	cp /data/projects/libytheana_mito/data/derived/libytheana_clipped.fasta .

# copy reads to current folder
cleaned_seqs.fastq: /data/projects/libytheana_mito/data/derived/cleaned_seqs.fastq
	cp /data/projects/libytheana_mito/data/derived/cleaned_seqs.fastq .

# index reference genome for bwa
libytheana_clipped.fasta.bwt: libytheana_clipped.fasta
	bwa index $<

# align reads to genome using bwa
cleaned_seqs.sai: libytheana_clipped.fasta.bwt libytheana_clipped.fasta cleaned_seqs.fastq
	bwa aln libytheana_clipped.fasta cleaned_seqs.fastq > cleaned_seqs.sai

# create sam file
cleaned_seqs_bwa.sam: libytheana_clipped.fasta cleaned_seqs.sai cleaned_seqs.fastq
	bwa samse libytheana_clipped.fasta cleaned_seqs.sai cleaned_seqs.fastq > cleaned_seqs_bwa.sam


## bowtie2
# build index for genome
libytheana_bowtie.4.bt2: libytheana_clipped.fasta
	./bowtie2-build libytheana_clipped.fasta libytheana_bowtie

# do alignment: bowtie <indexFile> <fastqfile> <outputFile>
cleaned_seqs_bowtie.sam: libytheana_bowtie.4.bt2 cleaned_seqs.fastq
	./bowtie2 -N 1 --mp 2 --local -x libytheana_bowtie -U cleaned_seqs.fastq -S cleaned_seqs_bowtie.sam


## samtools
# index the reference genome
libytheana_clipped.fasta.fai: libytheana_clipped.fasta
	@echo "### index the reference genome ###"
	samtools faidx libytheana_clipped.fasta

# convert bwa SAM to BAM file
cleaned_seqs_bwa.bam: libytheana_clipped.fasta.fai cleaned_seqs_bwa.sam
	@echo "### convert bwa SAM to BAM file ###"
	samtools import libytheana_clipped.fasta.fai cleaned_seqs_bwa.sam cleaned_seqs_bwa.bam

# sort the bwa BAM file
cleaned_seqs_bwa_sorted.bam: cleaned_seqs_bwa.bam
	@echo "### sort the BAM file ###"
	samtools sort $<  $@

# convert bowtie SAM to BAM file
cleaned_seqs_bowtie.bam: libytheana_clipped.fasta.fai cleaned_seqs_bowtie.sam
	@echo "### convert bowtie SAM to BAM file ###"
	samtools import libytheana_clipped.fasta.fai cleaned_seqs_bowtie.sam cleaned_seqs_bowtie.bam

# sort the bowtie BAM file
cleaned_seqs_bowtie_sorted.bam: cleaned_seqs_bowtie.bam
	@echo "### sort the bowtie BAM file ###"
	samtools sort $<  cleaned_seqs_bowtie_sorted

# index the BAM file

