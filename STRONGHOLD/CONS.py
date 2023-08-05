massive = {}
nucl = ['A', 'C', 'G', 'T']

# читаем FASTA file, оконачанием ввода данных слуджит 'ъ'
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


# возвращаем наиболее встречающееся азотистое основание (АО)
def max_n(a):
    if max(a['A'], a['C'], a['G'], a['T']) == a['A']:
        return 'A'
    elif max(a['A'], a['C'], a['G'], a['T']) == a['C']:
        return 'C'
    elif max(a['A'], a['C'], a['G'], a['T']) == a['G']:
        return 'G'
    else:
        return 'T'


read_FASTA()
seq_len = len(massive[0])
num_of_seq = len(massive)

ans = {'A': 'A: ', 'C': 'C: ', 'G': 'G: ', 'T': 'T: '}
cons_seq = ''

for i in range(seq_len):
    count = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

    # находим наиболее встречающееся АО
    for j in range(num_of_seq):
        count[massive[j][i]] += 1
    cons_seq += max_n(count)

    # добавляем данные в матрицу
    for j in nucl:
        ans[j] += str(count[j])
        ans[j] += ' '

# вывод ответа
print(cons_seq)

# вывод таблицы значений
for i in nucl:
    print(ans[i])