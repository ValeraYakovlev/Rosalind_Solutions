import math
import itertools

# подсчитываем количество строк, которые возможно получить переставлениями
a = int(input())
print(math.factorial(a))

b = a * [0]
# добавляем первый вариант строки
for i in range(a):
    b[i] = i + 1

# при помощи сторонней библиотеки делаем всевозможные переставления
c = itertools.permutations(b)

for i, j in enumerate(list(c)):
    permutation = ''
    for item in j:
        permutation += str(item) + ' '
    print(permutation)


