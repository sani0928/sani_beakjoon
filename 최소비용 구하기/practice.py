import sys; sys.stdin = open("input.txt")
import heapq

N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
start, end = map(int, input().split())

INF = float('inf')
dist = [INF] * (N + 1)
dist[start] = 0

# 누적비용, 시작위치
pq = [(0, start)]

while pq:

    cost, position = heapq.heappop(pq)
    # 현재 누적비용이 이전 누적비용보다 크면 탐색할 필요 X
    if cost > dist[position]:
        continue
    # 현재 위치가 도착지라면 while문 탈출
    if position == end:
        break
    # 현재 간선에서 all of 이동할 간선과 가중치
    for v, w in graph[position]:
        # 누적비용 + 이동할 간선의 가중치
        ncost = cost + w
        # 그게 더 적은 비용이라면 그걸로 교체
        if ncost < dist[v]:
            dist[v] = ncost
            heapq.heappush(pq, (ncost, v))

ans.append(dist[end])

