n = int(input())
k = int(input())

ans = n
for i in range(1, k):
    ans *= (n - i)

print(ans % 10**6)
