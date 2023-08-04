from Bio import SeqIO
massive = {}


def read_FASTA():
    c = 0
    with open("rosalind_kmer.txt", "r") as fa:
        for seq_record in SeqIO.parse(fa, "fasta"):
            massive[c] = str(seq_record.seq)
            c += 1


# переводим введеную строку с символами в dic формат для более удобной работы
def str_to_dic(a):
    ans = {}
    count = 0
    ans[count] = ''
    for i in a:
        if i == ' ':
            count += 1
            ans[count] = ''
        else:
            ans[count] += i
    return ans


"""рекурсионная функция, которая к каждому варианту длины n - 1 добавляет еще m вариантов
на 1 шаге, допустим возвращает А, тогда на втором шаге, если s = AB, вернет AA AB и т.д. 
в итоге выдает строку длиной n"""


def variants(d, rep):
    if rep == 1:
        buf = {0: dic[d]}
        return buf
    else:
        n_dic = {}
        c = 0
        prev = variants(d, rep - 1)
        for i in range(len(prev)):
            for j in dic:
                n_dic[c] = ''
                n_dic[c] = prev[i] + dic[j]
                c += 1
        return n_dic


s_b = 'A C G T'
n = 4
dic = str_to_dic(s_b)
cc = {}

# от каждого символа запускает рекурсионную функцию и выводит ее результат
# а именно все строки длиной n, начинающиеся с символа dic[i]
for i in dic:
    ans = variants(i, n)
    for j in ans:
        cc[ans[j]] = 0

read_FASTA()
s = massive[0]

#test
#s = 'CTTCGAAAGTTTGGGCCGAGTCTTACAGTCGGTCTTGAAGCAAAGTAACGAACTCCACGGCCCTGACTACCGAACCAGTTGTGAGTACTCAACTGGGTGAGAGTGCAGTCCCTATTGAGTTTCCGAGACTCACCGGGATTTTCGATCCAGCCTCAGTCCAGTCTTGTGGCCAACTCACCAAATGACGTTGGAATATCCCTGTCTAGCTCACGCAGTACTTAGTAAGAGGTCGCTGCAGCGGGGCAAGGAGATCGGAAAATGTGCTCTATATGCGACTAAAGCTCCTAACTTACACGTAGACTTGCCCGTGTTAAAAACTCGGCTCACATGCTGTCTGCGGCTGGCTGTATACAGTATCTACCTAATACCCTTCAGTTCGCCGCACAAAAGCTGGGAGTTACCGCGGAAATCACAG'
for i in range(0, len(s) - 3):
    cc[s[i: i + 4]] += 1

ans = ''
for i in cc:
    ans += str(cc[i]) + ' '

print(ans)