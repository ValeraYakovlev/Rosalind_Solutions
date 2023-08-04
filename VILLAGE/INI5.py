r_path = 'rosalind_ini5.txt'
with open(r_path, 'r') as r:
    read = []
    # читаем исходный файл
    for line in r:
        read.append(line.strip())

w_path = 'working_with_file_output.txt'
with open(w_path, 'w') as w:
    # записываем в файл все нечетные строки
    for i in range(1, len(read), 2):
        w.write(read[i] + '\n')
