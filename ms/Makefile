.PHONY: help

SCRIPTS = ../scripts
DATA = ../data
PRIMARY_DATA = ../data/primary
DERIVED_DATA = ../data/derived

help:
	@echo 'Makefile for the documentation                                    '
	@echo '                                                                  '
	@echo 'Usage:                                                            '
	@echo '                                                                  '
	@echo 'make clean_seqs                     Cleans the iontorrent reads   '

clean_seqs: $(DERIVED_DATA)/reads_without_indexes.fastq

$(DERIVED_DATA)/reads_without_indexes.fastq: $(SCRIPTS)/cleaning_script.py $(PRIMARY_DATA)/CarlosJul2015/CarlosJul2015.fastq
	python $< $(word 2,$^) $@
