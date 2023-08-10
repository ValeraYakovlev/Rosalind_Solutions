from Bio import SeqIO

# путь до входного файла
r_path = 'path'
massive = {}

# читаем FASTA файл
def read_FASTA():
    c = 0
    with open(r_path, "r") as fa:
        for seq_record in SeqIO.parse(fa, "fasta"):
            massive[c] = str(seq_record.seq)
            c += 1


read_FASTA()

# обозначаем какие есть последовательности
DNA_1 = massive[0]
DNA_2 = massive[1]


ans = ''
first = DNA_2[0]
# находим начальный символ из DNA2 в DNA1
num_s = DNA_1.find(first)
ans += str(num_s + 1) + ' '

i = 1

# проходим всю DNA_2
while i < len(DNA_2):
    # чтобы номера всегда возрастали, задаем j так (+ момент оптимизации)
    j = int(num_s) + 1
    while j < len(DNA_1):
        if DNA_2[i] == DNA_1[j]:
            ans += str(j + 1) + ' '
            num_s = j
            break
        j += 1
    i += 1

print(ans)