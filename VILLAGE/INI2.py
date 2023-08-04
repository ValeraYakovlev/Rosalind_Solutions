# переводим числа, раздленные пробелом, из строки в отдельные числа
def string_to_int():
    n = ''
    for i in nums:
        if i == ' ':
            dig.append(int(n))
            n = ''
        else:
            n += i
    dig.append(int(n))


dig = []
nums = input()
string_to_int()

# выводим квадрат гипотенузы
print(dig[0] ** 2 + dig[1] ** 2)

