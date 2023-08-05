from math import log10 as l

inp = {}
prob = {}
seq = ''
with open("rosalind_prob.txt", "r") as f:
    c = 0
    for line in f:
        inp[c] = line.replace("\n", "")
        c += 1


def transform():
    c = 0
    ans = ''
    for i in inp[1]:
        if i == ' ':
            prob[c] = ans
            ans = ''
            c += 1
        else:
            ans += i
    prob[c] = ans
    for key in prob:
        prob[key] = float(prob[key])


seq = inp[0]
transform()
otv = {}
c = 0
for key in prob:
    ans = 0
    for i in seq:
        if i == 'C' or i == 'G': ans += l(prob[key] / 2)
        else: ans += l((1 - prob[key]) / 2)
    otv[c] = ans
    c += 1

for i in otv:
    print('%.3f' % otv[i], end= ' ')