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


s = input()
nums = input()
dig = []
string_to_int()
# выводим строку с заданными границами
print(s[dig[0]: dig[1] + 1], s[dig[2]: dig[3] + 1])
