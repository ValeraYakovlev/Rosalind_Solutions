# переводим введеную строку в числа
def string_to_int():
    n = ''
    for i in nums:
        if i == ' ':
            dig.append(int(n))
            n = ''
        else:
            n += i
    dig.append(int(n))


nums = input()
dig = []
string_to_int()

# переводим числа из введенной строки в k и n
n = dig[0]
k = dig[1]

# начальные данные
ans = [0] * (n + 1)
ans[1] = 1

# для n-нного месяца считаем количество пар
for i in range(2, n + 1):
    ans[i] = ans[i - 1] + ans[i - 2] * k

print(ans[n])