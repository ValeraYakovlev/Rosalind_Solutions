# перевод кодона -> аминокислота
translater = {"UUU":"F", "CUU":"L", "AUU":"I", "GUU":"V",
              "UUC":"F", "CUC":"L", "AUC":"I", "GUC":"V",
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

DNA = input()

# ставим начало, тем самым накладывая рамку считывания
start = DNA.find('AUG')
amino_acid = ''

ans = ''

# с шагом в 3 азотистых основания идем по РНК и переводим их в аминокислоты
while amino_acid != 'Stop':
    codon = DNA[start:start + 3]
    amino_acid = translater[codon]
    if amino_acid == 'Stop': break
    else:
        ans += amino_acid
        start += 3

print(ans)
