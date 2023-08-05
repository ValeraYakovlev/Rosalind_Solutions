# ввод данных
a = input()
b = input()

ans = ''

# поиск подпоследовательности
for i in range(len(a) - len(b)): #for i in range(len(a))
    if a[i:i + len(b)] == b:
        ans += str(i + 1)
        ans += ' '

# вывод полученного ответа
print(ans)