from Bio import SeqIO

# функция для подсчета GC-content для одной строки
def GC_content(seq):
    count = 0
    for i in seq:
        if i == 'C' or i == 'G':
            count += 1
    # переводим в проценты
    local_GC = (count / len(seq)) * 100
    return local_GC


# читаем входные данные и записываем их в dictionary records
records = {}
r_path = '/Users/valerijakovlev/Desktop/inputs/rosalind_gc-4.txt'
with open(r_path, 'r') as inp:
    for seq_record in SeqIO.parse(inp, 'fasta'):
        records[seq_record.id] = seq_record.seq

global_GC = -1
max_GC_id = ''

# находим id последовательности с максимальным значением GC-content
for i in records:
    if GC_content(records[i]) > global_GC:
        global_GC = GC_content(records[i])
        max_GC_id = i

w_path = 'GC_output.txt'
with open(w_path, 'w') as w:
    w.write(max_GC_id + '\n' + str('%.6f' % global_GC))
