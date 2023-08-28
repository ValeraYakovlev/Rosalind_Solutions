from Bio import SeqIO

# чтение FASTA
ans = []
r_path = '/Users/valerijakovlev/Desktop/inputs/rosalind_cat.txt'
with open(r_path, 'r') as fa:
    for seq_record in SeqIO.parse(fa, 'fasta'):
        ans.append(str(seq_record.seq))


def dp_max(a, b):
    local_max = -1
    for i in range(a + 1, b):
        summ = dp[a][i] + dp[i + 1][j]
        if summ > local_max:
            local_max = summ
    return local_max


# n1 - nucleotide1; n2 - nucleotide2
def complement(n1, n2):
    comp = {'A': 'U', 'U': 'A', 'C': 'G', 'G': 'C'}
    return comp[n1] == n2


seq = ans[0]
#seq = 'GGGAAAUCC'
n = len(seq)

dp = [[0 for _ in range(n + 2)] for _ in range(n + 2)]

# Nussinov algorithm
for t in range(1, n + 2):
    for i in range(1, n - t + 2):
        j = i + t - 1
        dp[i][j] = (max(dp[i + 1][j], dp[i][j - 1], dp[i + 1][j - 1] + complement(seq[i - 1], seq[j - 1]), dp_max(i, j)))


#print(*dp, sep='\n')
lm = -1
for i in dp:
    for j in i:
        if j > lm:
            lm = j
print(lm)
print(1 % 1000000)
print(seq)