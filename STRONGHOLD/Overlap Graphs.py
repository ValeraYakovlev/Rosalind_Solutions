from Bio import SeqIO

with open("/Users/valerijakovlev/Desktop/proga/rosalind_grph.txt") as f:
    fasta_sequences = list(SeqIO.parse(f, 'fasta'))

# к - шаг, которым мы сравниеваем
k = 3

# делаем полный перебор всех первых пар и вторых пар
# у которых совпадают суффиксы и префиксы
for fasta_1 in fasta_sequences:
    for fasta_2 in fasta_sequences:
        # вычлиняем из FASTA файла название последовательности и саму последовательность
        name_1, seq_1 = fasta_1.id, fasta_1.seq
        name_2, seq_2 = fasta_2.id, fasta_2.seq
        if seq_1 != seq_2:
            # первые k символов
            preff = seq_1[-k:]
            # последние k символов
            suff = seq_2[:k]
            if preff == suff:
                print(name_1, name_2)

