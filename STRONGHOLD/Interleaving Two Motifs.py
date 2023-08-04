from Bio import SeqIO

#massive = {}


"""def read_FASTA():
    c = 0
    with open("", "r") as fa:
        for seq_record in SeqIO.parse(fa, "fasta"):
            massive[c] = str(seq_record.seq)
            c += 1
"""


# test
#s1 = 'ATCTGAT'
#s2 = 'TGCATA'

# real
s1 = 'GTTGGGGCTTACTTGCGATCAGTGACATGACGAGCACGATGATCATTGTGCCTCACAGCGGAATCCCCCCATCGAAGCTTATCT'
s2 = 'TTTTGGAGATGGTGACCCCAACTGATGCAAATGACTTTTTTCACCGTCGTATCTTGAGATCCGACCAATGCGATACGGAGGCACTCGCCCCATGG'


def rev(s):
    otv = ''
    for i in reversed(s):
        otv += i
    return otv


def ans(a, b):
    n = len(a)
    m = len(b)
    dyn = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] != b[j - 1]:
                dyn[i][j] = max(dyn[i - 1][j], dyn[i][j - 1])
            else:
                dyn[i][j] = dyn[i - 1][j - 1] + 1

    for i in range(len(dyn)):
        print(dyn[i])

    ans = ''

    while n > 0 or m > 0:
        if n == 0:
            ans += b[m - 1]
            m -= 1
        elif m == 0:
            ans += a[n - 1]
            n -= 1
        else:
            if dyn[n][m] == dyn[n - 1][m]:
                ans += a[n - 1]
                n -= 1
            elif dyn[n][m] == dyn[n][m - 1]:
                ans += b[m - 1]
                m -= 1
            else:
                ans += a[n - 1]
                n -= 1
                m -= 1

    return rev(ans)


print(ans(s1, s2))