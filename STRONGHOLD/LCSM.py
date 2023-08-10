from Bio import SeqIO

# путь до входного файла
r_path = 'path'
massive = {}

# читаем FASTA файл
def read_FASTA():
    c = 0
    with open(r_path, "r") as fa:
        for seq_record in SeqIO.parse(fa, "fasta"):
            massive[c] = str(seq_record.seq)
            c += 1



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


