from Bio import SeqIO
massive = {}


def read_FASTA():
    c = 0
    with open("rosalind_pdst.txt", "r") as fa:
        for seq_record in SeqIO.parse(fa, "fasta"):
            massive[c] = str(seq_record.seq)
            c += 1


# ищем разнницу между строками s1 и s2 и выводим это в виде коэффа (разница / длина строки)
def diff_finding(s1, s2):
    l = len(s1)
    diff = 0
    for i in range(l):
        if s1[i] != s2[i]:
            diff += 1
    return diff / l


read_FASTA()
n = len(massive)
ans = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        ans[i][j] = diff_finding(massive[i], massive[j])

for i in range(n):
    for j in range(n):
        print("%.5f" % ans[i][j], end=' ')
    print()






