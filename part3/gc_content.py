from pyfaidx import Fasta
import sys

def compute_gc_content(sequence):
    sequence = sequence.upper()
    n_c = sequence.count("C")
    n_g = sequence.count("G")

    return (n_c + n_g) / len(sequence)

def compute_gc_content_on_region(fasta_file_name, chromosome, start, end):
    ref = Fasta(fasta_file_name)
    dna = str(ref[chromosome][start:end])

    return compute_gc_content(dna)


def main():
    fasta = sys.argv[1]
    chromosome = sys.argv[2]
    start = int(sys.argv[3])
    end = int(sys.argv[4])

    print(compute_gc_content_on_region(fasta, chromosome, start, end))
