from funcs import read_FASTA
path = "rosalind_kmp.txt"
read = read_FASTA(path)[0]
ans = [0] * len(read)

max_motif_l = 0
# k = i + j - 1
for i in range(1, len(read)):
    for j in range(1, len(read) - i + 1):
        #print(read[:i], read[j: i + j], read[:i] == read[j: i + j])
        if read[:i] == read[j: i + j]:
            ans[j + i - 1] = len(read[:i])
            max_motif_l = len(read[:i])
    if max_motif_l < len(read[:i]):
        break

for i in ans:
    print(i, end=" ")