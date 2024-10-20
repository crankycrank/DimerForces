#!/usr/bin/env python3

import sys
import argparse
from Bio import SeqIO
import wordcount as wc

parser = argparse.ArgumentParser(
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    description='Compute CpG force for sequences in a fasta file')
parser.add_argument('fasta_infile', help='input FASTA file')

args = parser.parse_args()

sys.stdout.write("id\tlength\tvalid_dimers\tCpG_force\n")
for rec in  SeqIO.parse(args.fasta_infile, "fasta"):
    seq = str(rec.seq).upper()
    N_Valid = wc.count_overlapping_words(seq, 2, normalize=False).sum()
    dForce = wc.DimerForce(seq, "CG")
    sys.stdout.write("{}\t{}\t{}\t{}\n".format(rec.id, len(seq), N_Valid,
        dForce))
