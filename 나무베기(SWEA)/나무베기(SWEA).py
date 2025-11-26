import sys; sys.stdin = open("나무베기(SWEA).txt")
from collections import deque

dr, dc = (-1,0,1,0), (0,1,0,-1)

T = int(input())
for tc in range(1, T + 1):
    ans = 10**9
    N, K = map(int, input().split())
    grid = [list(map(str, input().strip())) for _ in range(N)]
    q = deque()
    vis = [[[0] * 4 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 'X':
                grid[i][j] = 'G'
                q.append((i, j, 0, 0, K))
                vis[i][j][0] = 1

                break
    while q:

        cr, cc, d, cnt, bomb = q.popleft()

        for k in range(-1,2,2):
            nd = (d + k) % 4
            if not vis[cr][cc][nd]:
                vis[cr][cc][nd] = 1
                q.append((cr, cc, nd, cnt + 1, bomb))

        nr, nc = cr + dr[d], cc + dc[d]
        if 0 <= nr < N and 0 <= nc < N:
            if grid[nr][nc] == 'T':
                if bomb:
                    q.append((nr, nc, d, cnt + 1, bomb - 1))
            elif grid[nr][nc] == 'G':
                q.append((nr, nc, d, cnt + 1, bomb))
            elif grid[nr][nc] == 'Y':
                ans = cnt + 1
                break

    if ans == 10**9:
        print(f'#{tc} -1')
    else:
        print(f'#{tc} {ans}')