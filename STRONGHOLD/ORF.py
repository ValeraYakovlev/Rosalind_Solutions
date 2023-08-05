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


def print_protein(start, f_RNA):
        ans = ''
        amino_acid = ''
        while amino_acid != 'Stop' and start < len(f_RNA) - 2:
            codon = f_RNA[start: start + 3]
            amino_acid = translater[codon]
            if amino_acid == 'Stop':
                break
            else:
                ans += amino_acid
                start += 3
        if amino_acid == 'Stop':
            if ans not in ans_base:
                ans_base[ans] = 1
                print(ans)



def read_FASTA():
    count = -1
    while 1:
        a = str(input())
        if a == 'ъ':
            break
        else:
            if 'Rosalind' in a:
                count += 1
                massive[count] = ''
            else:
                massive[count] += a


def create_RNA(s):
    RNA_code = {'A': 'U', 'C': 'G', 'G': 'C', 'T': 'A'}
    R = ''.join(RNA_code[k] for k in reversed(s))
    return R


def create_compl_DNA(s):
    DNA_code = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    D = ''.join(DNA_code[k] for k in reversed(s))
    return D


read_FASTA()

RNA_1 = create_RNA(massive[0])
RNA_2 = create_RNA(create_compl_DNA(massive[0]))

ans_base = {}

for i in range(len(RNA_1) - 2):
    if RNA_1[i: i + 3] == 'AUG':
        print_protein(i, RNA_1)

for i in range(len(RNA_2) - 2):
    if RNA_2[i: i + 3] == 'AUG':
        print_protein(i, RNA_2)

