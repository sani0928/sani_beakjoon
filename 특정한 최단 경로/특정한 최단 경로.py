import sys; sys.stdin = open("특정한 최단 경로.txt")

input = sys.stdin.readline

N, E = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(E):
    u, v, c = map(int, input().split())
    graph[u].append((v, c))
    graph[v].append((u, c))

INF = 100**9
v1, v2 = map(int, input().split())
dist = [[INF for _ in range(N+1)] for _ in range(N+1)]
dist[1][1] = 0

for i in range(1, N+1):
    for v, c in graph[i]:
        dist[i][v] = c
        dist[v][i] = c

visited = [False] * (N + 1)
ans = INF

def go(pos, necessary, total):
    global graph, ans

    if v1 in necessary and v2 in necessary and necessary[-1] == N:
        # print(necessary)
        # print('total', total)
        if ans > total:
            ans = total
        return

    for v, _ in graph[pos]:
        if not visited[v]:
            visited[v] = True
            necessary.append(v)
            go(v, necessary, total + dist[pos][v])
            necessary.pop()
            visited[v] = False

    return

go(1, [], 0)
if ans != INF:
    print(ans)
else:
    print(-1)
