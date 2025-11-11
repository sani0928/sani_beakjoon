import sys; sys.stdin = open("외판원_순회_2.txt")

def go(u, cnt, cost, vis, start):
    global min_cost

    if cost >= min_cost:
        return

    if cnt == N:
        if grid[u][start] != 0:
            min_cost = min(min_cost, cost + grid[u][start])
        return

    for v in range(N):
        if not vis[v] and grid[u][v] != 0:
            vis[v] = True
            go(v, cnt + 1, cost + grid[u][v], vis, start)
            vis[v] = False
    return

N = int(input())
min_cost = 10**9
grid = [list(map(int, input().split())) for _ in range(N)]
for s in range(N):
    visited = [False] * N
    visited[s] = True
    go(s, 1, 0, visited, s)
print(min_cost)