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