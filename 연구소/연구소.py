import sys; sys.stdin = open("연구소.txt")
from collections import deque
dr, dc = (0,1,0,-1), (1,0,-1,0)
N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
vis = [[False] * M for _ in range(N)]
no_wall_spot = []

for r in range(N):
    for c in range(M):
        if grid[r][c] == 1:
            vis[r][c] = True
        elif grid[r][c] == 0:
            no_wall_spot.append((r, c))

ans = 0
def bfs_and_cnt():

    q = deque()
    virus_vis = [[0] * M for _ in range(N)]
    for r in range(N):
        for c in range(M):
            if grid[r][c] == 2:
                virus_vis[r][c] = 2
                q.append((r, c))
            elif vis[r][c]:
                virus_vis[r][c] = 1

    while q:
        cr, cc = q.popleft()
        for k in range(4):
            nr, nc = cr + dr[k], cc + dc[k]
            if 0 <= nr < N and 0 <= nc < M:
                if virus_vis[nr][nc] == 0:
                    virus_vis[nr][nc] = 2
                    virus_vis[nr][nc] = 2
                    q.append((nr, nc))

    cnt = 0
    for rr in range(N):
        for cc in range(M):
            if virus_vis[rr][cc] == 0:
                cnt += 1
    return cnt

def back(idx, walls):
    global ans

    if walls == 3:
        cnt = bfs_and_cnt()
        ans = max(ans, cnt)
        return

    for i in range(idx, len(no_wall_spot)):
        r, c = no_wall_spot[i]
        if not vis[r][c]:
            vis[r][c] = True
            # 안전영역 갯수
            back(idx + 1, walls + 1)
            vis[r][c] = False
    return

back(0, 0)
print(ans)