from Bio import SeqIO


def count_noncross(rna):
    if len(rna) <= 2:
        return 1
    else:
        if rna in dic:
            return dic[rna]

        subsequences = []
        for i in range(1, len(rna)):
            if rna[0] == complement[rna[i]] and check_subseq(rna[1:i]):
                subsequences.append([rna[1:i], rna[i + 1:]])
        if not subsequences:
            dic[rna] = 0
        else:
            dic[rna] = sum(count_noncross(subseq[0]) * count_noncross(subseq[1]) for subseq in subsequences)

        return dic[rna]


def check_subseq(subseq):
    if subseq.count('A') == subseq.count('U') and subseq.count('G') == subseq.count('C'):
        return True
    return False


# чтение FASTA
ans = []
r_path = '/Users/valerijakovlev/Desktop/inputs/rosalind_cat-2.txt'
with open(r_path, 'r') as fa:
    for seq_record in SeqIO.parse(fa, 'fasta'):
        ans.append(str(seq_record.seq))

#seq = ans[0]
seq = 'AUAUGCA'
dic = {}
complement = {'A': 'U', 'U': 'A', 'C': 'G', 'G': 'C'}
mod = 10 ** 6
w_path = '/Users/valerijakovlev/Desktop/outputs/CAT_output.txt'
with open(w_path, 'w') as w:
    w.write(str(count_noncross(seq) % mod))




