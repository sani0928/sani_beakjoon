import sys; sys.stdin = open("아기_상어_2.txt")
from collections import deque

dr, dc = (0,1,1,1,0,-1,-1,-1), (1,1,0,-1,-1,-1,0,1)
def calculation(sr, sc):
    global ans

    min_dist = 10**9
    q = deque([(sr, sc, 0)])
    vis = [[False] * M for _ in range(N)]
    vis[sr][sc] = True

    while q:
        cr, cc, t = q.popleft()
        for k in range(8):
            nr, nc = cr + dr[k], cc + dc[k]
            if 0 <= nr < N and 0 <= nc < M and not vis[nr][nc]:
                vis[nr][nc] = True
                if grid[nr][nc] == 1:
                    min_dist = min(min_dist, t + 1)
                q.append((nr, nc, t + 1))

    return min_dist

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
ans = 0

for i in range(N):
    for j in range(M):
        if grid[i][j] == 0:
            ans = max(ans, calculation(i,j))

print(ans)