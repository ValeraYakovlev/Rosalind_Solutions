from Bio import SeqIO
from math import factorial as fact

# чтение FASTA
ans = []
r_path = '/Users/valerijakovlev/Desktop/inputs/rosalind_mmch.txt'
with open(r_path, 'r') as fa:
    for seq_record in SeqIO.parse(fa, 'fasta'):
        ans.append(str(seq_record.seq))

# cчитаем кол-во каждых нуклеотидов
seq = ans[0]
nucl = {'A': 0, 'U': 0, 'C': 0, 'G': 0}
for i in seq:
    nucl[i] += 1

# среди комплементарных находим кого больше и меньше
AU_max = max(nucl['A'], nucl['U'])
AU_min = min(nucl['A'], nucl['U'])

GC_max = max(nucl['G'], nucl['C'])
GC_min = min(nucl['G'], nucl['C'])

"""
чтобы понять эту формулу, рассмотрим закономерность:
s = AAAU
количество способов соединить 3

s = AAAUU
количество способов соеденить 6

Нетрудно доказать, что количество способов = (кол-во A)! / ((кол-во A) - (кол-во U))!
"""
ans = (fact(AU_max) // fact(AU_max - AU_min)) * (fact(GC_max) // fact(GC_max - GC_min))

# записываем ответ
w_path = '/Users/valerijakovlev/Desktop/outputs/MMCH_output.txt'
with open(w_path, 'w') as w:
    w.write(str(ans))