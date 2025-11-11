import sys; sys.stdin = open("유기농_배추.txt")
from collections import deque

def searching():
    for r in range(N):
        for c in range(M):
            if grid[r][c] == 1 and not vis[r][c]:
                return r, c
    return -1, -1

def bfs():
    while q:
        cr, cc = q.popleft()
        for k in range(4):
            nr, nc = cr + dr[k], cc + dc[k]
            if 0 <= nr < N and 0 <= nc < M and not vis[nr][nc]:
                if grid[nr][nc] == 1:
                    vis[nr][nc] = True
                    q.append((nr, nc))
    return

dr, dc = (0,1,0,-1), (1,0,-1,0)
T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    grid = [[0] * M for _ in range(N)]
    vis = [[False] * M for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        grid[y][x] = 1

    ans = 0
    while True:
        sr, sc = searching()
        if sr == -1 and sc == -1:
            break
        q = deque([(sr, sc)])
        vis[sr][sc] = True
        bfs()
        ans += 1

    print(ans)
