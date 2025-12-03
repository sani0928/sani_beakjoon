import sys; sys.stdin = open("창용_마을_무리의_개수(SWEA).txt")

# def find(x):
#
#     if x != parent[x]:
#         parent[x] = find(parent[x])
#     return parent[x]
#
# def union(a,b):
#
#     a = find(a)
#     b = find(b)
#
#     if a < b:
#         parent[b] = parent[a]
#     else:
#         parent[a] = parent[b]
#     return
#
# T = int(input())
# for tc in range(1, T + 1):
#     N, M = map(int, input().split())
#     parent = list(range(N + 1))
#     edges = []
#     for _ in range(M):
#         u, v = map(int, input().split())
#         edges.append((u, v))
#     edges.sort()
#
#     for u, v in edges:
#         if find(u) != find(v):
#             union(u, v)
#
#     print(parent)
#
#     print(f'#{tc} {len(set(parent[1:]))}')
from collections import deque
def dfs(x):
    global vis

    q = deque([x])
    vis[x] = True

    while q:

        u = q.popleft()
        if graph[u]:
            for v in graph[u]:
                if not vis[v]:
                    vis[v] = True
                    q.append(v)
    return

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    vis = [False] * (N + 1)
    ans = 0

    for _ in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)

    for i in range(1, N + 1):
        if not vis[i]:
            dfs(i)
            ans += 1

    print(f'#{tc} {ans}')