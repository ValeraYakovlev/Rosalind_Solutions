fib = [0, 1]

try:
    # до какого числа нужен вывод; если такого нет, напишите '-'
    n = int(input())

    # заполнение массива числами из ряда Фибоначчи до n позиции включительно
    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])

    # вывод через запятую чисел из ряда Фибоначчи до n позиции включительно
    for i in range(n + 1):
        if i != n:
            print(fib[i], end=', ')
        else:
            print(fib[i])
except:
    c = 2
    print(f'{fib[0]}, {fib[1]}, ', end='')
    while True:
        fib.append(fib[c - 1] + fib[c - 2])
        print(fib[c], end=', ')
        c += 1
