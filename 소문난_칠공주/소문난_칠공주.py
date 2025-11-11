import sys; sys.stdin = open("소문난_칠공주.txt")
from collections import deque
dr, dc = (0,1,0,-1), (1,0,-1,0)

grid = [list(input()) for _ in range(5)]
vis = [[False] * 5 for _ in range(5)]
ans = 0

def go(r, c, lst):
    global ans

    if len(lst) == 7:
        print(lst)
        cnt = 0
        for r,c in lst:
            if grid[r][c] == 'S':
                cnt += 1
        if cnt >= 4:
            print(lst)
            ans += 1
        return

    for k in range(4):
        nr, nc = r + dr[k], c + dc[k]
        if 0 <= nr < 5 and 0 <= nc < 5 and not vis[nr][nc]:
            vis[nr][nc] = True
            lst.append((nr, nc))
            go(nr, nc, lst)
            lst.pop()
            vis[nr][nc] = False
for r in range(5):
    for c in range(5):
        q = deque([(r,c)])
        go(r, c, q)
print(ans)