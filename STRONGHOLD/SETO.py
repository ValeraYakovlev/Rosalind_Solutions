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
