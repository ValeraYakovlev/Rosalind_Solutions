n = int(input())
m = int(input())
a = {}
i = 1

# пишем ДП-шечку
# m - молодая особь, M - взрослая особь
while i <= n:
    if i == 1:
        a[i] = {'m': 1, 'M': 0}
    else:
        if i <= m:
            a[i] = {'m': a[i - 1]['M'], 'M': a[i - 1]['m'] + a[i - 1]['M']}
        else:
            a[i] = {'m': a[i - 1]['M'], 'M': a[i - 1]['m'] + a[i - 1]['M'] - a[i - m]['m']}
    i += 1

print(a[n]['m'] + a[n]['M'])
