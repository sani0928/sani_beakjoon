import sys; sys.stdin = open("도시_건설.txt")

N, M = map(int, input().split())
parent = list(range(N + 1))
size = [1] * (N + 1)
edges = []
all_cost = 0
min_cost = 0
cnt = 0
for i in range(M):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))
    all_cost += c

edges.sort()

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(x, y):
    a = find_parent(x)
    b = find_parent(y)

    if a == b:
        return False

    if size[a] < size[b]:
        parent[a] = b
        size[b] += size[a]
    else:
        parent[b] = a
        size[a] += size[b]
    return True

for i in range(M):
    cost, u, v = edges[i]
    if union_parent(u, v):
        min_cost += cost
        cnt += 1

if cnt == N - 1:
    print(all_cost - min_cost)
else:
    print(-1)
