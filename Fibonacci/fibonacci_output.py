# рекуресивная функция, возвращающая число Фибоначчи на n позиции
def fibonacci(num):
    if num == 1 or num == 0:
        return num
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)


# до какого числа нужен вывод
n = int(input())

# вывод через запятую чисел из ряда Фибоначчи до n позиции включительно
for i in range(n + 1):
    if i != n:
        print(fibonacci(i), end=', ')
    else:
        print(fibonacci(i))
