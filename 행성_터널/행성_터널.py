import sys; sys.stdin = open("행성_터널.txt")

def go(start):
    global graph, dist

    x1, y1, z1 = graph[start]
    min_dist = 10 ** 9
    check = None

    for k in range(1, N + 1):
        if k == start:
            continue
        if dist[k] != 10 ** 9:
            continue
        x2, y2, z2 = graph[k]
        temp = min(min_dist, abs(x1 - x2), abs(y1 - y2), abs(z1 - z2))
        if temp < min_dist:
            min_dist = temp
            check = k
    dist[check] = min_dist

N = int(input())
parent = list(range(N + 1))
graph = [(0,0,0)]
for i in range(1, N + 1):
    x, y, z = map(int, input().split())
    graph.append((x, y, z))
dist = [10 ** 9] * (N + 1)

for i in range(1, N + 1):
    go(i)
print(sum(dist[1:N]))
print(dist)