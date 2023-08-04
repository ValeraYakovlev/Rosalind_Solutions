# test
s = '51423'

mas = {}
#s = {}


# переводим строку в удобный тип хранения данных - dict
def trans():
    otv = ''
    c = 0
    for i in mas[0]:
        if i == ' ':
            s[c] = int(otv)
            otv = ''
            c += 1
        else:
            otv += i
    s[c] = int(otv)


with open("test_lis.txt", "r") as f:
    c = 0
    n = int(f.readline())
    for line in f:
        mas[c] = line
        c += 1

#trans()


def find_inc():
    l = len(s)
    dyn = [[0] * (l + 1) for _ in range(l + 1)]
    dyn[0][0] = 1
    for i in range(1, l + 1):
        pr = s[i - 1]
        for j in range(1, l + 1):
            dyn[i][j] = max(dyn[i][j - 1], dyn[i - 1][j], dyn[i - 1][j - 1])
            if s[j - 1] < pr:
                dyn[i][j] += 1
                pr = s[j - 1]
    for i in range(len(dyn)):
        print(dyn[i])
    n, m = l, l
    ans = ''
    while n > 0 or m > 0:
        if dyn[n - 1][m] == dyn[n][m]: n -= 1
        elif dyn[n][m - 1] == dyn[n][m]: m -= 1
        else:
            print(ans, m)
            ans += str(s[m - 1]) + ' '
            n -= 1
            m -= 1

    print(ans)


find_inc()