import sys; sys.stdin = open("특정_거리의_도시_찾기.txt")
from collections import deque

input = sys.stdin.readline
N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)

answer = []
q = deque([(X,0)])
vis = [10**9] * (N+1)
vis[X] = 0

while q:

    u, t = q.popleft()

    if t == K:
        answer.append(u)
        continue

    for v in graph[u]:
        if vis[v] > t + 1:
            vis[v] = t + 1
            q.append((v, t + 1))

answer.sort()
if answer:
    for ans in answer:
        print(ans)
else:
    print(-1)