massive = {}

# читаем FASTA файл; окончание рида означает ввод 'ъ'
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


# функция, которая возвращает строку нужной длины
def substrings(n, m):
    return shortest[n:m]


read_FASTA()
# поиск наименьшей строки в massive
shortest = min(massive.values(), key=len)

# цикл идет от максимальной длины строки, до минимальной, при нахождении общей строки
# в данном случае, она и будет самой максимальной по длине

for i in range(len(shortest)):
    for j in range(i + 1):
        sub = substrings(j, len(shortest) - i + j)
        est = True

        # смотрим наличие подстроки в других строках
        for k in range(len(massive)):
            if sub not in massive[k]:
                est = False

                # момент оптимизации, ускоряет работу кода в несколько раз
                break

        # если значение не было переключено на false - значит мы нашли нужную подстроку - выводим ее
        if est:
            print(sub)
            quit()


