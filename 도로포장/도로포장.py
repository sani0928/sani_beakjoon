import sys; sys.stdin = open("도로포장.txt")

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

N, M, K = map(int, input().split())
edges = []
for _ in range(M):
    u, v, t = map(int, input().split())
    edges.append((t, u, v))

edges.sort(reverse=True)
parent = list(range(N+1))

print(edges)
dist = [0] * (N + 1)
ans = 0
for time, u, v in edges:
    if find(u) != find(v):
        union(u, v)
        ans += time
        print(u, v)
        print(parent)
        if find(1) == find(N):
            break

print(ans)