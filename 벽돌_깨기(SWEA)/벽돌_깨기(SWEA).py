import sys; sys.stdin = open("벽돌_깨기(SWEA).txt")
from collections import deque
import copy

dr, dc = (0,1,0,-1), (1,0,-1,0)

# 후보 블록 제거
def clean(candi, new_grid):

    for r,c in candi:
        new_grid[r][c] = 0
    return

# 블록 내리기
def down(new_grid):

    for c in range(W):
        arr = []
        for r in range(H):
            if  new_grid[r][c] != 0:
                arr.append(new_grid[r][c])

        col = [0] * (H - len(arr)) + arr
        for r in range(H):
            new_grid[r][c] = col[r]
    return

# 폭팔 후보 지정 및 후보 블록 제거 후 블록 내리기
def bomb(grid, sr, sc):

    new_grid = copy.deepcopy(grid)

    q = deque([(sr, sc)])
    candidate = [(sr, sc)]
    vis = [[False] * W for _ in range(H)]
    vis[sr][sc] = True

    while q:

        cr, cc = q.popleft()
        for i in range(new_grid[cr][cc]):
            for k in range(4):
                nr, nc = cr + dr[k]*i, cc + dc[k]*i
                if 0 <= nr < H and 0 <= nc < W:
                    if new_grid[nr][nc] != 0 and not vis[nr][nc]:
                        vis[nr][nc] = True
                        candidate.append((nr, nc))
                        q.append((nr, nc))

    clean(candidate, new_grid)
    down(new_grid)
    return new_grid

# 남은 블록 계산
def check(grid):

    cnt = 0
    for r in range(H-1,-1,-1):
        for c in range(W-1,-1,-1):
            if grid[r][c] != 0:
                cnt += 1
    return cnt

# N번 반복
def back(grid, deep):
    global ans

    if check(grid) == 0:
        ans = 0
        return

    if deep == N:
        ans = min(ans, check(grid))
        return

    for c in range(W):
        for r in range(H):
            if grid[r][c] != 0:
                new_grid = bomb(grid, r, c)
                back(new_grid, deep + 1)
                break

T = int(input())
for tc in range(1, T + 1):
    N, W, H = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(H)]

    ans = 10**9

    back(board,0)

    print(f'#{tc} {ans}')