import sys; sys.stdin = open("플로이드.txt")
import heapq

input = sys.stdin.readline

N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

INF = 100**9
for i in range(1, N+1):
    dist = [INF] * (N + 1)
    dist[i] = 0
    pq = []
    pq = [(0, i)]

    while pq:

        cost, u = heapq.heappop(pq)

        if cost > dist[u]:
            continue

        for v, w in graph[u]:
            ncost = cost + w
            if ncost < dist[v]:
                # print(f'현재 노드: {u}, 다음 노드: {v}, 총 금액: {ncost}')
                dist[v] = ncost
                heapq.heappush(pq, (ncost, v))

    for fix in range(N + 1):
        if dist[fix] == INF:
            dist[fix] = 0
    print(*dist[1:])