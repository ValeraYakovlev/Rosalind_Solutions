population = {}
for i in range(6):
    population[i] = int(input())

"""
0: AA-AA dominance 100%
1: aa-AA dominance 100%
2: AA-aa dominance 100%
3: Aa-Aa dominance 75%
4: Aa-aa dominance 50%
5: aa-aa dominance 0%
"""
dominance = {0: 1, 1: 1, 2: 1, 3: 3/4, 4: 1/2, 5: 0}


ans = 0
for i in range(6):
    ans += dominance[i] * population[i]

print(ans * 2)