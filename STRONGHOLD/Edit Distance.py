from Bio import SeqIO
massive = {}


def solve():
    s1 = massive[0]
    s2 = massive[1]

    dyn = [[0] * (len(s2) + 1) for i in range(len(s1) + 1)]
    for i in range(len(s1) + 1): dyn[i][0] = i
    for j in range(len(s2) + 1): dyn[0][j] = j

    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] != s2[j - 1]:
                up = dyn[i - 1][j] + 1
                dow = dyn[i][j - 1] + 1
                diag = dyn[i - 1][j - 1] + 1
                dyn[i][j] = min(up, dow, diag)
            else:
                up = dyn[i - 1][j] + 1
                dow = dyn[i][j - 1] + 1
                diag = dyn[i - 1][j - 1]
                dyn[i][j] = min(up, dow, diag)

    return dyn[len(s1)][len(s2)]


def read_FASTA():
    c = 0
    with open("rosalind_edit-3.txt", "r") as fa:
        for seq_record in SeqIO.parse(fa, "fasta"):
            massive[c] = str(seq_record.seq)
            c += 1


read_FASTA()
print(solve())
