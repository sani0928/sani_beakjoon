import sys; sys.stdin = open("이분_그래프.txt")
from collections import deque
t = int(input())
for _ in range(t):

    V, E = map(int, input().split())
    painting = [0] * (V + 1)
    graph = [[] for _ in range(V + 1)]

    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    stop = False
    for start in range(1, V+1):
        if painting[start] != 0:
            continue
        painting[start] = 1
        q = deque([start])

        while q and not stop:
            u = q.popleft()
            for v in graph[u]:
                if painting[v] == 0:
                    painting[v] = -painting[u]
                    q.append(v)
                elif painting[u] == painting[v]:
                    stop = True
                    break

    print('YES' if not stop else 'NO')
