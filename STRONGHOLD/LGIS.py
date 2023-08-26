r_path = '/Users/valerijakovlev/Desktop/inputs/rosalind_lgis-3.txt'
with open(r_path, 'r') as r:
    n = int(r.readline().strip())
    pre_arr = r.readline().split()
    arr = []
    for i in pre_arr:
        arr.append(int(i))

"""arr = [5, 1, 4, 2, 3]
n = len(arr)"""
dp_inc = n * [1]
prev_inc = n * [-1]

for i in range(1, n):
    for j in range(0, i):
        if arr[i] > arr[j] and dp_inc[i] <= dp_inc[j]:
            dp_inc[i] = dp_inc[j] + 1
            prev_inc[i] = j

max_length_inc = max(dp_inc)
last_inc = dp_inc.index(max_length_inc)

ans_inc = []
while True:
    ans_inc.append(arr[last_inc])
    last_inc = prev_inc[last_inc]
    if last_inc == -1:
        break

dp_decr = n * [1]
prev_decr = n * [-1]

for i in range(1, n):
    for j in range(0, i):
        if arr[i] < arr[j] and dp_decr[i] <= dp_decr[j]:
            dp_decr[i] = dp_decr[j] + 1
            prev_decr[i] = j

max_length = max(dp_decr)
last_decr = dp_decr.index(max_length)

ans_decr = []
while True:
    ans_decr.append(arr[last_decr])
    last_decr = prev_decr[last_decr]
    if last_decr == -1:
        break

w_path = '/Users/valerijakovlev/Desktop/outputs/LGIS_output.txt'
with open(w_path, 'w') as w:
    for i in reversed(ans_inc):
        w.write(str(i) + ' ')
    w.write('\n')
    for i in reversed(ans_decr):
        w.write(str(i) + ' ')

