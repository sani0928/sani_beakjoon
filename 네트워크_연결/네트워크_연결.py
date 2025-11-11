import sys; sys.stdin = open("네트워크_연결.txt")

N = int(input())
M = int(input())
parent = list(range(N+1))
edges = []
for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))
edges.sort()
min_cost = 0

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    return

for i in range(M):
    cost, u, v = edges[i]
    if find_parent(parent, u) != find_parent(parent, v):
        union_parent(parent, u, v)
        min_cost += cost

print(min_cost)