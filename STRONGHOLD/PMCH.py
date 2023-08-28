from math import factorial as fact
from Bio import SeqIO

# чтение FASTA
ans = []
r_path = '/Users/valerijakovlev/Desktop/inputs/rosalind_pmch.txt'
with open(r_path, 'r') as fa:
    for seq_record in SeqIO.parse(fa, 'fasta'):
        ans.append(str(seq_record.seq))

r_seq = ans[0]
A = 0
C = 0
for i in r_seq:
    if i == 'A':
        A += 1
    elif i == 'C':
        C += 1

# количество способов сделать пары АТ - A! GC - C! общее количество (A!) * (C!)
w_path = '/Users/valerijakovlev/Desktop/outputs/PMCH_output.txt'
with open(w_path, 'w') as w:
    w.write(str(fact(A) * fact(C)))