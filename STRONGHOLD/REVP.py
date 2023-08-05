massive = {}
code = {'A':'T', 'C':'G', 'G':'C', 'T':'A'}


# читаем FASTA файл, конец ввода - 'ъ'
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

# переодим type reversed -> в str
def find_reverse(s):
    n_s = ''
    for i in s:
        n_s += code[i]
    return n_s

# проверяем являются ли строки палиндромами
def find_palindrome(s):
    r_s = find_reverse(reversed(s))
    if r_s == s:
        return True
    else:
        return False


read_FASTA()
for i in range(len(massive[0])):
    k = 4
    while k <= 12 and i + k <= len(massive[0]):
        mas = massive[0][i:(i + k)]
        # как только нашли палиндром - выводим его
        if find_palindrome(mas):
            print(i + 1, k)
        k += 1
