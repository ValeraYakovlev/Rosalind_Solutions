# две последовательности, одинаковой длины
seq1 = input()
seq2 = input()

ans = 0

for i in range(len(seq1)):
    if seq1[i] != seq2[i]:
        ans += 1

print(ans)