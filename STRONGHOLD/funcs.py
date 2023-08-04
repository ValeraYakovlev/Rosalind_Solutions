from Bio import SeqIO


def read_FASTA(seq):
    massive = {}
    c = 0
    with open(seq, "r") as fa:
        for seq_record in SeqIO.parse(fa, 'fasta'):
            massive[c] = str(seq_record.seq)
            c += 1
    return massive
