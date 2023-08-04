path = 'rosalind_seto-2.txt'
with open(path, "r") as r:
    n = int(r.readline())
    pre_s1 = r.readline().strip()
    pre_s2 = r.readline().strip()

for i in ['{', '}']:
    pre_s1 = pre_s1.replace(i, '')
    pre_s2 = pre_s2.replace(i, '')

A = set(int(i) for i in pre_s1.split(', '))
B = set(int(i) for i in pre_s2.split(', '))

U = set()
for i in range(n): U.add(i + 1)

print(A | B)
print(A & B)
print(A - B)
print(B - A)
print(U - A)
print(U - B)




"""def print_ans(a):
    print('{', end='')
    for i in a:
        if i == max(a):
            print(i, end='}')
        else:
            print(f'{i},', end=' ')
    print()


def union():
    buff = {}
    for i in max(s1, s2, key=len):
        buff[i] = 1
    if buff == s1:
        for i in s2:
            if i not in s1:
                buff[i] = 1
    else:
        for i in s1:
            if i not in s2:
                buff[i] = 1
    print_ans(buff)
    return buff


def A_B():
    buff_s1 = {}
    for i in s1:
        buff_s1[i] = 1
    for i in inter:
        buff_s1.pop(i)
    print_ans(buff_s1)


def B_A():
    buff_s2 = {}
    for i in s2:
        buff_s2[i] = 1
    for i in inter:
        buff_s2.pop(i)
    print_ans(buff_s2)


def U_A():
    buff_u = {}
    for i in U:
        buff_u[i] = 1
    for i in s1:
        buff_u.pop(i)
    print_ans(buff_u)


def U_B():
    buff_u = {}
    for i in U:
        buff_u[i] = 1
    for i in s2:
        buff_u.pop(i)
    print_ans(buff_u)


def intersection():
    buff = {}
    for i in min(s1, s2, key=len):
        buff[i] = 1
    if buff == s1:
        for i in s1:
            if i not in s2:
                buff.pop(i)
    else:
        for i in s2:
            if i not in s1:
                buff.pop(i)
    print_ans(buff)
    return buff


def to_dic(s, a):
    num = ''
    for i in s:
        if i != '{' and i != '}':
            if i == ',':
                a[int(num)] = 1
                num = ''
            else:
                num += i
    a[int(num)] = 1


with open(path, "r") as r:
    n = int(r.readline())
    c = 0
    strings = []
    for line in r:
        strings.append(line.replace('\n', ''))

s1 = {}
s2 = {}
to_dic(strings[0], s1)
to_dic(strings[1], s2)

U = {}
for i in range(n):
    U[i + 1] = 1

union()
inter = intersection()
A_B()
B_A()
U_A()
U_B()"""
