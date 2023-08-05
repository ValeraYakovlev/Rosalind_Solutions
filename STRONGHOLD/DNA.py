seq = input()
A = 0
C = 0
G = 0
T = 0

for i in seq:
    if i == 'A': A += 1
    elif i == 'C': C += 1
    elif i == 'G': G += 1
    else: T += 1

print(A, C, G, T)