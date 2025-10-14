import sys; sys.stdin = open("빙산.txt")
from collections import deque

# 빙산 갯수 체크
def check():

    cnt = 0
    lst = []

    for i in range(N):
        for j in range(M):
            if grid[i][j] != 0:
                cnt2 = 0
                for k in range(4):
                    nr, nc = i + dr[k], j + dc[k]
                    if 0 <= nr < N and 0 <= nc < M:
                        if grid[nr][nc] == 0:
                            cnt2 += 1
                lst.append((i,j,cnt2))
                cnt += 1

    return cnt, lst

def searching_ice():

    for i2 in range(N):
        for j2 in range(M):
            if grid[i2][j2] != 0:
                return i2, j2

    return -1, -1

# 빙산 덩어리 체크
def bfs(sr, sc):

    q = deque([(sr, sc)])
    visited = [[False] * M for _ in range(N)]
    visited[sr][sc] = True

    cnt = 1

    while q:

        cr, cc = q.popleft()

        for k in range(4):
            nr, nc = cr + dr[k], cc + dc[k]
            if 0 <= nr < N and 0 <= nc < M:
                if not visited[nr][nc] and grid[nr][nc] != 0:
                    visited[nr][nc] = True
                    cnt += 1
                    q.append((nr, nc))

    return cnt

def after_one_year(save):

    for rr, cc, cnt in save:
        grid[rr][cc] -= cnt
        if grid[rr][cc] < 0:
            grid[rr][cc] = 0

    return

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
dr, dc = (0,1,0,-1), (1,0,-1,0)
ans = 0

while True:

    chek, save = check()
    sr, sc = searching_ice()
    if sr == -1 and sc == -1:
        print(0)
        break

    chek2 = bfs(sr, sc)

    if chek == chek2:
        after_one_year(save)
        ans += 1
    else:
        print(ans)
        break



