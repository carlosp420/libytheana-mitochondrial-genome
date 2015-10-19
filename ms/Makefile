.PHONY: help

SCRIPTS = ../scripts
DATA = ../data
PRIMARY_DATA = ../data/primary
DERIVED_DATA = ../data/derived

help:
	@echo 'Makefile for the documentation                                         '
	@echo '                                                                       '
	@echo 'Usage:                                                                 '
	@echo '                                                                       '
	@echo 'make clean_seqs                     Cleans the iontorrent reads        '
	@echo 'make manuscript                     Renders the manuscript as PDF file '

clean_seqs: $(DERIVED_DATA)/reads_without_indexes.fastq

$(DERIVED_DATA)/reads_without_indexes.fastq: $(SCRIPTS)/cleaning_script.py $(PRIMARY_DATA)/CarlosJul2015/CarlosJul2015.fastq
	python $< $(word 2,$^) $@


#
# make manuscript in PDF
#
#
manuscript: ms.pdf

ms.pdf: header.latex ms.md refs.bib zookeys.csl
	pandoc --latex-engine=xelatex -s -S --template header.latex -f markdown -V geometry:a4paper -V geometry:margin=1in ms.md \
				--bibliography=refs.bib --csl=zookeys.csl -o ms.pdf

