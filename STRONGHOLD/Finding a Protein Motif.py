import requests as r
from Bio import SeqIO
from io import StringIO

mas = {}
protein_seq = {}


def read_file():
    with open("rosalind_mprt.txt", "r") as f:
        c = 0
        for line in f:
            if len(line) > 1:
                mas[c] = line.replace('\n', '')
                c += 1


"""
Эта функция - вынужденная мера, так как сайт uniport поменяли то, как должно выглядеть обращение к данным, например
вместо:
https://www.uniprot.org/uniprot/P07204_TRBM_HUMAN

нужно

https://www.uniprot.org/uniprot/P07204

как видим - для обращения, нужно все имя до '_' эта функция вычленяет нужный кусок из имени

"""
def correct_name(s):
    name = ''
    for i in s:
        if i == '_': break
        else: name += i
    return name


"""
в этом FASTA файле в id и name хранились следующие данные:
какая-то инфа|имя|какая-то инфа
эта функция, вычленяет нужное имя
"""
def get_name(a):
    first = False
    ans = ''
    for i in a:
        if not first:
            if i == '|':
                first = True
        else:
            if i == '|': break
            else: ans += i
    return ans


# обращаемся к uniport за интересующей нас последовательностью
def get_seq():
    for key in mas:
        name = mas[key]
        url = 'https://www.uniprot.org/uniprot/' + correct_name(mas[key]) + '.fasta'
        response = r.post(url)
        cData = ''.join(response.text)

        Seq = StringIO(cData)
        pSeq = list(SeqIO.parse(Seq, 'fasta'))
        for seq_record in pSeq:
            protein_seq[name] = seq_record.seq


def check(fi, se, th, fo):
    motif = False
    if fi == 'N':
        if se != 'P' and fo != 'P':
            if th == 'S' or th == 'T':
                motif = True
    # все эти if, нужны, чтобы проверить, является ли motif N{P}[ST]{P} или нет
    return motif


read_file()
get_seq()

for key in protein_seq:
    s = protein_seq[key]
    ans = ''
    for i in range(len(s) - 3):
        if check(s[i], s[i + 1], s[i + 2], s[i + 3]): ans += str(i + 1) + ' '

    if len(ans) != 0:
        print(key)
        print(ans[0: len(ans) - 1])