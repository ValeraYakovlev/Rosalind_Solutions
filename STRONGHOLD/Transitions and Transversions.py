from Bio import SeqIO
massive = {}


def read_FASTA():
    c = 0
    with open("rosalind_tran.txt", "r") as fa:
        for seq_record in SeqIO.parse(fa, "fasta"):
            massive[c] = str(seq_record.seq)
            c += 1


read_FASTA()
DNA_1 = massive[0]
DNA_2 = massive[1]

#test
#DNA_1 = 'GCAACGCACAACGAAAACCCTTAGGGACTGGATTATTTCGTGATCGTTGTAGTTATTGGAAGTACGGGCATCAACCCAGTT'
#DNA_2 = 'TTATCTGACAAAGAAAGCCGTCAACGGCTGGATAATTTCGCGATCGTGCTGGTTACTGGCGGTACGAGTGTTCCTTTGGGT'
transitions = 0
transversions = 0

for i in range(len(DNA_1)):
    if DNA_1[i] != DNA_2[i]:
        # смотрим, если изменени пурин - пурин; пиримидин - пиримидин
        if DNA_1[i] == 'A' and DNA_2[i] == 'G' or DNA_1[i] == 'G' and DNA_2[i] == 'A' or DNA_1[i] == 'C' and DNA_2[i] == 'T' or DNA_1[i] == 'T' and DNA_2[i] == 'C':
            transitions += 1
        else:
            transversions += 1

print("%.11f" % (transitions / transversions))

