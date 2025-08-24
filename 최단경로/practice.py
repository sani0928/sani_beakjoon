import sys; sys.stdin = open("input.txt")
import heapq

V, E = map(int, input().split())
start_node = int(input())
graph = [[] for _ in range(V + 1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

INF = float('inf')
dist = [INF] * (V + 1)
dist[start_node] = 0

pq = [(0, start_node)]

while pq:

    cost, u = heapq.heappop(pq)

    if cost > dist[u]:
        continue

    for v, w in graph[u]:
        ncost = cost + w
        if ncost < dist[v]:
            dist[v] = ncost
            heapq.heappush(pq, (ncost, v))

for i in range(1, V + 1):
    if dist[i] == INF:
        ans.append('INF')
    else:
        ans.append(dist[i])