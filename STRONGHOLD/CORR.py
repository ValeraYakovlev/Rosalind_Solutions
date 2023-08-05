from funcs import read_FASTA
# путь по которому хранятся риды
path = 'rosalind_corr.txt'
# получаем риды и записываем их в dict
reads = read_FASTA(path)

nucleotides = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'} # комлементарные АО
similarities = {} # словарь для записи данных формата {строка: номера последовательностьей с ней}
no_pair = {} # номера строк, не записанных в similarites
h_pair = {} # номера строк, записанных в similarites


# функция, которая к строке 3' seq1 5' выдает комплементарную ей, ориентированную также 3' comp_seq1 5'
def add_compliment(s):
    r_s = ''
    for i in reversed(s):
        r_s += nucleotides[i]
    return r_s


# функция, которая проверяет две строки на различия и если у них разница в 1 нуклеотид - выводит их
def find_right(seq1, seq2):
    ans = False
    for i in range(len(seq1)):
        for j in range(len(seq2)):
            if d_dist(seq1[i], seq2[j]) == 1:
                print(f'{seq1[i]}->{seq2[j]}')
                ans = True
                return ans
    return ans


# функция, которая к изначальным ридам, добавляет комлементраные им
def add_to_reads():
    for key in reads:
        seq = reads[key]
        reads[key] = {0: seq, 1: add_compliment(seq)}


# проверяет два рида (прямые и комлементарные) на сходство
def find_similar(a, b):
    same = False
    for i in range(2):
        for j in range(2):
            if a[i] == b[j]:
                #print(a[i], b[j])
                same = True
    return same


# высчитывает d_distance - посимвольная разница
def d_dist(s1, s2):
    ans = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            ans += 1
    return ans


# дополняет списки h_pair и no_pair
def find_np():
    all_seq = {}

    for i in range(len(reads)):
        all_seq[i] = 1

    for seq in similarities:
        nums = similarities[seq]
        for j in nums:
            all_seq.pop(nums[j])
            h_pair[nums[j]] = 1
    return all_seq


add_to_reads()
l_r = len(reads)
# цикл идет так, чтобы исключить сравнения i == j и, например 1 2 и 2 1, таким образом каждый раз i j уникальны и не
# получаются переставлением. в случа 1 2 и 2 1 - можно переставить и получится 1 2 1 2
for i in range(l_r):
    c = 0
    first = True
    for j in range(i + 1, l_r):
        seq = reads[i][0]
        if find_similar(reads[i], reads[j]) and first:
            similarities[seq] = {}
            similarities[seq][c] = i
            c += 1
            similarities[seq][c] = j
            c += 1
            first = False
        elif find_similar(reads[i], reads[j]):
            similarities[seq][c] = j
            c += 1

#print(similarities, '\n')
no_pair = find_np()

# ищем для последовательностей без пар, последовательности с парами
for key1 in no_pair:
    for key2 in h_pair:
        s1 = reads[key1]
        s2 = reads[key2]
        if find_right(s1, s2):
            break


