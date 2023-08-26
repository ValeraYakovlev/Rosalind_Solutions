import itertools

r_path = '/Users/valerijakovlev/Desktop/inputs/rosalind_lexv.txt'
with open(r_path, 'r') as r:
    s = r.readline().replace(' ', '').strip()
    n = int(r.readline().strip())

# cоздаем перестановки длиной от 1 до n из имеющихся символов s
perm = []
for i in range(1, n + 1):
    for j in list(itertools.product(s, repeat=i)):
        perm.append(''.join(map(str, j)))

# cортируем перестановки по индекску т.е. лексикографически
srt_perm = sorted(perm, key=lambda symbol: [s.index(c) for c in symbol])

w_path = '/Users/valerijakovlev/Desktop/outputs/LEXV_output.txt'
with open(w_path, 'w') as w:
    for i in srt_perm:
        w.write(''.join(map(str, i)) + '\n')
