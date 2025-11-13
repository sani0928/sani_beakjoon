import sys; sys.stdin = open("와드.txt")
from collections import deque
dr, dc = (0,1,0,-1,0), (1,0,-1,0,0)

def ward(r, c, region):

    q = deque([(r, c)])
    vis = [[False] * C for _ in range(R)]
    ans[r][c] = '.'
    vis[r][c] = True

    while q:
        r1, c1 = q.popleft()
        for kk in range(4):
            r2, c2 = r1 + dr[kk], c1 + dc[kk]
            if 0 <= r2 < R and 0 <= c2 < C:
                if grid[r2][c2] == region and not vis[r2][c2]:
                    vis[r2][c2] = True
                    ans[r2][c2] = '.'
                    q.append((r2, c2))
    return

R, C = map(int, input().split())
grid = [list(map(str, input().strip())) for _ in range(R)]
cr, cc = map(int, input().split())
cr -= 1; cc -= 1
ans = [['#'] * C for _ in range(R)]
cmd = list(map(str, input().strip()))
for c in cmd:
    if c == 'U':
        cr -= 1
    elif c == 'D':
        cr += 1
    elif c == 'L':
        cc -= 1
    elif c == 'R':
        cc += 1
    else:
        ward(cr, cc, grid[cr][cc])

for k in range(5):
    nr, nc = cr + dr[k], cc + dc[k]
    if 0 <= nr < R and 0 <= nc < C:
        ans[nr][nc] = '.'

for chunk in ans:
    print(*chunk)