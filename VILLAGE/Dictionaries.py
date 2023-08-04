with open('rosalind_ini6.txt', 'r') as r:
    read = []
    for line in r:
        read.append(line.strip())
s = read[0]
ans = {}
word = ''
for i in s:
    if i == ' ':
        if word not in ans:
            ans[word] = 1
        else:
            ans[word] += 1
        word = ''
    else:
        word += i
if word not in ans:
    ans[word] = 1
else:
    ans[word] += 1
word = ''

with open('Dictionaries_output.txt', 'w') as w:
    for key in ans:
        w.write(key + ' '+ str(ans[key]) + ' \n')
