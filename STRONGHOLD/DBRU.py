def complem(s):
    ans = ''
    for i in reversed(s):
        ans += nucl[i]
    return ans

# комплементарные нуклеотиды
nucl = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

r_path = '/Users/valerijakovlev/Desktop/inputs/rosalind_dbru.txt'
st = set()
check = []
# создаем множество строк
with open(r_path, 'r') as r:
    for line in r:
        check.append(line.strip())
        st.add(line.strip())

# создаем множество обратных комплементов
rev_st = set()
for i in st:
    rev_st.add(complem(i))

union_set = st | rev_st
ans = set()

# из строки a, длиной k + 1 делаем суффикс и префикс длиной k
for i in union_set:
    n = len(i)
    ans.add((i[:(n - 1)], i[1:]))

w_path = '/Users/valerijakovlev/Desktop/outputs/DBRU_output.txt'
with open(w_path, 'w') as w:
    for i in ans:
        w.write('(' + i[0] + ', ' + i[1] + ')' + '\n')

