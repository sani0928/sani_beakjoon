import sys; sys.stdin = open("우주신과의_교감.txt")
import math

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    a = find(x)
    b = find(y)

    if a < b:
        parent[y] = x
    else:
        parent[x] = y
    return

N, M = map(int, input().split())
spots = []
parent = list(range(N+1))

for i in range(1, N + 1):
    x, y = map(int, input().split())
    spots.append((i, x, y))

for _ in range(M):
    u, v = map(int, input().split())
    union(u, v)

edges = []
ans = 0
for i, x, y in spots:
    for i2, x2, y2 in spots:
        if i != i2:
            if x == x2:
                dist = abs(y-y2)
            elif y == y2:
                dist = abs(x-x2)
            else:
                dist = math.sqrt(abs(x-x2)**2 + abs(y-y2)**2)
            edges.append((dist, i, i2))

edges.sort()
print(edges)
for cost, u, v in edges:

    if find(u) != find(v):
        print(u, v)

        union(u, v)
        ans += cost

print("{:.2f}".format(ans))