import sys; sys.stdin = open("모래성.txt")
from collections import deque
H, W = map(int, input().split())
grid = [list(input().strip()) for _ in range(H)]
check = [[0] * W for _ in range(H)]
dr, dc = (0,1,1,1,0,-1,-1,-1), (1,1,0,-1,-1,-1,0,1)
time = 0
q = deque()

for r in range(H):
    for c in range(W):
        if grid[r][c] == '.':
            q.append((r, c))

while True:
    cnt = 0
    for _ in range(len(q)):
        cr, cc = q.popleft()
        for k in range(8):
            nr, nc = cr + dr[k], cc + dc[k]
            if 0 <= nr < H and 0 <= nc < W:
                if grid[nr][nc] != '.':
                    check[nr][nc] += 1
                    if check[nr][nc] >= int(grid[nr][nc]):
                        cnt += 1
                        grid[nr][nc] = '.'
                        q.append((nr, nc))
    if cnt == 0:
        break

    time += 1

print(time)