from math import factorial as f


def c_n_k(a, b):
    return f(a) / (f(b) * f(a - b))


k = int(input())
n = int(input())

p = 4.0/16
q = 1 - p
print(p, q)
al = 2 ** k
print(al)
ans = []
for i in range(n, (al + 1)):
    ans.append(c_n_k(al, i) * 0.25**i * 0.75**(al - i))
print(ans)
print(sum(ans))
