def str_to_num():
    num = ''
    for i in string_nums:
        if i == ' ':
            nums.append(float(num))
            num = ''
        else:
            num += i
    nums.append(float(num))


# функция для подсчета GC-content для одной строки
def GC_prob_count(GC):
    GC_prob = 1
    for i in seq:
        if i == 'C' or i == 'G':
            GC_prob *= (GC / 2)
        else:
            GC_prob *= ((1 - GC) / 2)
    return GC_prob


r_path = '/Users/valerijakovlev/Desktop/inputs/rosalind_eval.txt'
read = [] # [0] - число n [1] - последовательность S [2] - CG-content
with open(r_path, 'r') as r:
    for line in r:
        read.append(line.strip())

n = int(read[0])
seq = read[1]
string_nums = read[2]

nums = []
str_to_num()
print(nums)

# сколько подпоследовательностьей seq может быть в строке t длинной n
possible_pos = n - len(seq) + 1

ans = []
for i in nums:
    ans.append('%.3f' % (GC_prob_count(i) * possible_pos))

w_path = '/Users/valerijakovlev/Desktop/outputs/EVAL_output.txt'
with open(w_path, 'w') as w:
    w.write(' '.join(map(str, ans)))

