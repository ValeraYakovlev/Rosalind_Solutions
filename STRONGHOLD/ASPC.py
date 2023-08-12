from math import factorial as f

n = int(input())
m = int(input())

ans = 0
# считаем все C из n по к для m =< k =< n
for k in range(m, n + 1):
    MOD = 10 ** 6
    n_f = f(n)
    k_f = f(k)
    nk_f = f(n - k)
    comb = n_f // (k_f * nk_f)
    ans += comb
    ans %= MOD

print(ans)