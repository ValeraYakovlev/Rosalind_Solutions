# переводим введеную строку с символами в dic формат для более удобной работы
def str_to_dic(a):
    ans = {}
    count = 0
    ans[count] = ''
    for i in a:
        if i == ' ':
            count += 1
            ans[count] = ''
        else:
            ans[count] += i
    return ans


"""рекурсионная функция, которая к каждому варианту длины n - 1 добавляет еще m вариантов
на 1 шаге, допустим возвращает А, тогда на втором шаге, если s = AB, вернет AA AB и т.д. 
в итоге выдает строку длиной n"""


def variants(d, rep):
    if rep == 1:
        buf = {0: dic[d]}
        return buf
    else:
        n_dic = {}
        c = 0
        prev = variants(d, rep - 1)
        for i in range(len(prev)):
            for j in dic:
                n_dic[c] = ''
                n_dic[c] = prev[i] + dic[j]
                c += 1
        return n_dic


s = input()
n = int(input())
dic = str_to_dic(s)

# от каждого символа запускает рекурсионную функцию и выводит ее результат
# а именно все строки длиной n, начинающиеся с символа dic[i]
for i in dic:
    ans = variants(i, n)
    for j in ans:
        print(ans[j])
