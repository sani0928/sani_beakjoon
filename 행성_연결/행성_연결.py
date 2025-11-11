import sys; sys.stdin = open("행성_연결.txt")

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    a = find(x)
    b = find(y)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    return

N = int(input())
cosmos = [list(map(int, input().split())) for _ in range(N)]
parent = list(range(N + 1))
edges = []
for i in range(N):
    for j in range(N):
        if i != j:
            edges.append((cosmos[i][j], i, j))
edges.sort()
ans = 0
for c, u, v in edges:
    if find(u) != find(v):
        union(u, v)
        ans += c
print(ans)