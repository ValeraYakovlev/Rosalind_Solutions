a = int(input())
b = int(input())
ans = 0
if a % 2 == 0:
    a += 1
for i in range(a, b + 1, 2):
    ans += i
print(ans)