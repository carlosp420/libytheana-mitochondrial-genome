"""Cleaning the IonTorrent reads by removing indexes and dropping reads shorter
than 20 bp.
"""
import re
import sys

from Bio import SeqIO

INDEX = 'AACAACAACC'


def remove_index(seq):
    seq = re.sub(INDEX, '', str(seq))
    return seq


if len(sys.argv) < 3:
    print("\nInput fastq sequence file to remove short reads (adapter dimers)")
    print(" and outputfile path")
    sys.exit(1)


fastq_file = sys.argv[1].strip()
output_file = sys.argv[2].strip()

output_reads = (seq_record[10:] for seq_record in SeqIO.parse(fastq_file, "fastq")
                if seq_record.seq.startswith(INDEX) and len(seq_record.seq[10:]) > 20)

count = SeqIO.write(output_reads, output_file, "fastq")
print("Saved {} reads".format(count))
