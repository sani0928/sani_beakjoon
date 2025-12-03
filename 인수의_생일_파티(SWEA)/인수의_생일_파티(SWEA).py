import sys; sys.stdin = open("인수의_생일_파티(SWEA).txt")
import heapq

def letsgo(start):

    min_dist = 10**9
    vis = [False] * (N + 1)

    q = []
    vis[start] = True
    for d, v in graph[start]:
        heapq.heappush(q, (d, v, 0))

    while q:
        d, arrived, time = heapq.heappop(q)
        vis[arrived] = True
        time += d
        if arrived == X:
            min_dist = min(min_dist, time)
            return min_dist
        else:
            for d, v in graph[arrived]:
                if not vis[v]:
                    heapq.heappush(q, (d, v, time))
    return min_dist

def letsgo2(end):

    min_dist = 10**9
    vis = [False] * (N + 1)

    q = []
    vis[X] = True
    for d, v in graph[X]:
        heapq.heappush(q, (d, v, 0))

    while q:
        d, arrived, time = heapq.heappop(q)
        vis[arrived] = True
        time += d
        if arrived == end:
            min_dist = min(min_dist, time)
            return min_dist
        else:
            for d, v in graph[arrived]:
                if not vis[v]:
                    heapq.heappush(q, (d, v, time))
    return min_dist


T = int(input())
for tc in range(1, T + 1):
    N, M, X = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        u, v, d = map(int, input().split())
        graph[u].append((d, v))

    ans = 0

    for u in range(1, N + 1):
        if u == X:
            continue
        # X를 제외한 노드의 최소 왕복 거리 계산
        dist = letsgo(u) + letsgo2(u)
        # 그 중 가장 긴 왕복 거리 갱신
        ans = max(ans, dist)

    print(f'#{tc} {ans}')

