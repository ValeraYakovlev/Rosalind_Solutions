import itertools
n = int(input())
arr = list(range(1, n + 1))

# всевозможные перестановки положительных чисел
pre_pos_perm = itertools.permutations(arr)

# всевозможные перестановки чисел -1, 1 длиной n
pre_minus_perm = itertools.product([-1, 1], repeat=n)

# переводим в list
pos_perm = []
for i in pre_pos_perm:
    pos_perm.append(list(i))

minus_perm = []
for i in pre_minus_perm:
    minus_perm.append(list(i))

global_ans = []
for i in pos_perm:
    for j in minus_perm:
        local_ans = []
        # перемножаем одно на другое и получаем всевозможные перестановки как положительных, так и отрицательных чисел
        for k in range(n):
            local_ans.append(i[k] * j[k])
        global_ans.append(local_ans)

w_path = '/Users/valerijakovlev/Desktop/outputs/SIGN_output.txt'
with open(w_path, 'w') as w:
    # записываем количество перестановок
    w.write(str(len(minus_perm) * len(pos_perm)) + '\n')
    # записываем в файл всевозможные перестановки
    for i in global_ans:
        w.write(' '.join(map(str, i)) + '\n')