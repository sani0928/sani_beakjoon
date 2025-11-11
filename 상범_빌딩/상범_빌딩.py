import sys; sys.stdin = open("상범_빌딩.txt")
from collections import deque

dr, dc = (0,1,0,-1,1,-1), (1,0,-1,0)
while True:
    L, R, C = map(int, input().split())
    if L == 0 and R == 0 and C == 0:
        break

    grid = []
    start = None

    for l in range(L):
        floor = []
        for r in range(R):
            row = list(input().strip())
            for c, char in enumerate(row):
                if char == 'S':
                    start = (l, r, c)
            floor.append(row)
        grid.append(floor)
        input()

    check = False
    time = 0
    sl, sr, sc = start
    q = deque([(sl, sr, sc, 0)])
    vis = [[[False] * C for _ in range(R)] for _ in range(L)]

    vis[sl][sr][sc] = True

    while q:
        ch, cr, cc, time = q.popleft()
        if grid[ch][cr][cc] == 'E':
            check = True
            break

        for k in range(6):
            if k == 4 or k == 5:
                nh, nr, nc = ch + dr[k], cr, cc,
            else:
                nh, nr, nc = ch, cr + dr[k], cc + dc[k]
            if 0 <= nh < L and 0 <= nr < R and 0 <= nc < C:
                if not vis[nh][nr][nc] and grid[nh][nr][nc] != '#':
                    vis[nh][nr][nc] = True
                    q.append((nh, nr, nc, time + 1))

    if check:
        print(f'Escaped in {time} minute(s).')
    else:
        print('Trapped!')