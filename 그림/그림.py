import sys; sys.stdin = open("그림.txt")
from collections import deque

dr, dc = (0,1,0,-1), (1,0,-1,0)
N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
vis = [[False] * M for _ in range(N)]
total, ans = 0, 0

def go(sr, sc):
    cnt = 0
    q = deque([(sr, sc)])
    vis[sr][sc] = True

    while q:
        cr, cc = q.popleft()
        cnt += 1
        for k in range(4):
            nr, nc = cr + dr[k], cc + dc[k]
            if 0 <= nr < N and 0 <= nc < M:
                if grid[nr][nc] == 1 and not vis[nr][nc]:
                    vis[nr][nc] = True
                    q.append((nr, nc))
    return cnt

for r in range(N):
    for c in range(M):
        if not vis[r][c] and grid[r][c] == 1:
            total += 1
            result = go(r, c)
            ans = max(ans, result)

print(total)
print(ans)