import sys; sys.stdin = open("나만_안되는_연애.txt")

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

N, M = map(int, input().split())
uni = [0] + list(map(str, input().split()))
parent = list(range(N+1))
ans = 0
cnt = 0
edges = []
for _ in range(M):
    u, v, dist = map(int, input().split())
    edges.append((dist, u, v))
edges.sort()
for d, u, v in edges:
    if find(u) != find(v) and uni[u] != uni[v]:
        union(u, v)
        ans += d
        cnt += 1

if cnt == N - 1:
    print(ans)
else:
    print(-1)
