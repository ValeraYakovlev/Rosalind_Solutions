with open("rosalind_tree.txt", "r") as f:
    n = int(f.readline())
    adjacency_list = [line.strip().split(" ") for line in f]

graph = [[0] * n for i in range(n)]
used = [0] * n


def dfs(v, l):
    used[v] = 1
    for i in range(l):
        if graph[v][i] == 1 and not used[i]:
            dfs(i, l)


# заполняем матрицу гррафа
for i in range(len(adjacency_list)):
    k = int(adjacency_list[i][0]) - 1
    m = int(adjacency_list[i][1]) - 1
    graph[k][m] = 1
    graph[m][k] = 1

comp = 0
# считаем количество компонентов связанности
for i in range(n):
    if not used[i]:
        dfs(i, n)
        comp += 1

# выводим количество ребер, нужно, чтобы связать эти компоненты связанности
print(comp - 1)


