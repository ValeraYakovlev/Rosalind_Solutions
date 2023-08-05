massive = {}

translater = {"UUU": "F", "CUU": "L", "AUU": "I", "GUU": "V",
              "UUC": "F", "CUC": "L", "AUC": "I", "GUC": "V",
              "UUA": "L", "CUA": "L", "AUA": "I", "GUA": "V",
              "UUG": "L", "CUG": "L", "AUG": "M", "GUG": "V",
              "UCU": "S", "CCU": "P", "ACU": "T", "GCU": "A",
              "UCC": "S", "CCC": "P", "ACC": "T", "GCC": "A",
              "UCA": "S", "CCA": "P", "ACA": "T", "GCA": "A",
              "UCG": "S", "CCG": "P", "ACG": "T", "GCG": "A",
              "UAU": "Y", "CAU": "H", "AAU": "N", "GAU": "D",
              "UAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D",
              "UAA": "Stop", "CAA": "Q", "AAA": "K", "GAA": "E",
              "UAG": "Stop", "CAG": "Q", "AAG": "K", "GAG": "E",
              "UGU": "C", "CGU": "R", "AGU": "S", "GGU": "G",
              "UGC": "C", "CGC": "R", "AGC": "S", "GGC": "G",
              "UGA": "Stop", "CGA": "R", "AGA": "R", "GGA": "G",
              "UGG": "W", "CGG": "R", "AGG": "R", "GGG": "G"}


def read_FASTA():
    pre_RNA = ''
    count = -1
    while 1:
        a = str(input())
        if a == 'ъ':
            break
        else:
            # записываем RNA
            if 'Rosalind' in a:
                count += 1
                if count != 0: massive[count] = ''
            # добавляем интроны в массив
            else:
                if count == 0: pre_RNA += a
                else: massive[count] += a

    return pre_RNA

# получаем RNA
RNA = read_FASTA()
# вырезаем все интроны
for i in massive:
    if massive[i] in RNA:
        RNA = RNA.replace(massive[i], '')

RNA = RNA.replace("T", "U")

protein = ''
start = RNA.find("AUG")

while True:
    # переводим кодон в аминокислоту
    c = RNA[start: start + 3]
    if translater[c] == 'Stop':
        break
    else:
        protein += translater[c]
        start += 3

print(protein)

