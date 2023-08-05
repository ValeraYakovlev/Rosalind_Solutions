from Bio import SeqIO
massive = {}


def read_FASTA():
    c = 0
    with open("rosalind_long.txt", "r") as fa:
        for seq_record in SeqIO.parse(fa, "fasta"):
            massive[c] = str(seq_record.seq)
            c += 1


def find_preff(a, b):
    ans = 0
    l = len(min(a, b, key=len))
    for i in range(l // 2, l):
        suff = a[-i:]
        preff = b[:i]
        if suff == preff:
            ans = i
    return ans


def dfs(x, c):
    used[x] = c
    for i in range(n):
        if graph[x][i] != 0 and used[i] == 0:
            dfs(i, c + 1)
            #ans[x][i] = c + 1


def create_superstring(a, s):
    nw = 0
    nxt = 0
    for i in range(n):
        if used[i] == a + 1:
            nw = i
        if used[i] == a + 2:
            nxt = i
    if a == 0:
        s += massive[nw]
    h = graph[nw][nxt]
    l = len(massive[nxt])
    #print(massive[nxt][-1 * (l - h):], '\n')
    s += massive[nxt][-1 * (l - h):]

    return s



read_FASTA()
n = len(massive)
graph = [[0] * n for _ in range(n)]

for i in massive:
    for j in massive:
        graph[i][j] = find_preff(massive[i], massive[j])

for i in range(len(graph)):
    print(graph[i])

stop = False

#ans = [[0] * n for _ in range(n)]
used = [0] * n

for i in range(n):
    if stop:
        break
    else:
        for j in range(n):
            if not stop:
                for k in range(n): used[k] = 0
                if graph[i][j] != 0:
                    dfs(i, 1)
                if max(used) == n:
                    stop = True

ans = ''
for i in range(n - 1):
    ans = create_superstring(i, ans)

print(ans)
