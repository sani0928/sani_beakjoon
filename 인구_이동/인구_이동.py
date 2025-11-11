import sys; sys.stdin = open("인구_이동.txt")
from collections import deque

dr, dc = (0,1,0,-1), (1,0,-1,0)
N, L, R = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
day = 0

def diff(a, b):
    global stop

    if L <= abs(a- b) <= R:
        stop = False
        return True
    else:
        return False

def bfs(r, c, num):

    lst = [(r, c)]
    total = grid[r][c]
    cnt = 1
    q = deque([(r, c)])

    while q:
        cr, cc = q.popleft()
        for k in range(4):
            nr, nc = cr + dr[k], cc + dc[k]
            if 0 <= nr < N and 0 <= nc < N:
                if diff(grid[cr][cc], grid[nr][nc]) and vis[nr][nc] == 0:
                    vis[nr][nc] = num
                    total += grid[nr][nc]
                    cnt += 1
                    q.append((nr, nc))
                    lst.append((nr, nc))

    for i, j in lst:
        grid[i][j] = total // cnt
    return

stop = False
while not stop:
    stop = True
    union = 0
    vis = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if vis[r][c] == 0:
                union += 1
                vis[r][c] = union
                bfs(r, c, union)
    if not stop:
        day += 1

    for ccc in vis:
        print(*ccc)
    print('--------')
    for cccc in grid:
        print(*cccc)
    print('--------')

print(day)