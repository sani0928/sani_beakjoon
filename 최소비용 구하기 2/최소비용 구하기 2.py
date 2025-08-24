import sys; sys.stdin = open("input.txt")
import heapq

input = sys.stdin.readline

N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
from_bus, at_bus = map(int, input().split())

INF = float('inf')
dist = [INF] * (N + 1)
parent = [0] * (N + 1)
dist[from_bus] = 0

# 시작 위치 이전은 없으니 임의로 0 입력
pq = [(0, from_bus)]

while pq:

    cost, u = heapq.heappop(pq)

    if cost > dist[u]:
        continue

    if u == at_bus:
        break

    for v, w in graph[u]:
        ncost = cost + w
        if ncost < dist[v]:
            dist[v] = ncost
            parent[v] = u
            heapq.heappush(pq, (ncost, v))

ans = []
start = at_bus
while start != 0:
    ans.append(start)
    start = parent[start]
ans.reverse()

ans.append(dist[at_bus])
ans.append(len(ans))
ans.append(*ans)