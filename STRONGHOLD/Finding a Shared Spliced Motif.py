massive = {}

# читаем FASTA файл, "ъ" означает окончание ввода
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


def find_m(DNA_1, DNA_2):
    dyn = [0] * (len(DNA_1) + 1)
    for i in range(len(DNA_1) + 1): dyn[i] = (len(DNA_2) + 1) * [0]

    for i in range(1, len(DNA_1) + 1):
        for j in range(1, len(DNA_2) + 1):
            if DNA_1[i - 1] == DNA_2[j - 1]: dyn[i][j] = dyn[i - 1][j - 1] + 1
            else: dyn[i][j] = max(dyn[i - 1][j - 1], dyn[i - 1][j], dyn[i][j - 1])

    pre_ans = ''
    i, j = len(DNA_1), len(DNA_2)
    while dyn[i][j] != 0:
        if dyn[i][j] == dyn[i - 1][j]: i -= 1
        elif dyn[i][j] == dyn[i][j - 1]: j -= 1
        else:
            pre_ans += DNA_1[i - 1]
            i -= 1
            j -= 1

    return rev(pre_ans)


def rev(a):
    ans = ''
    for i in reversed(a):
        ans += i
    return ans


read_FASTA()
n = massive[0]
m = massive[1]
print(find_m(n, m))
