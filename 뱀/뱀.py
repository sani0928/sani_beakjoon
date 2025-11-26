import sys; sys.stdin = open("뱀.txt")
from collections import deque
dr, dc = (0,1,0,-1), (1,0,-1,0)

# 몸은 1, 사과는 2
N = int(input())
grid = [[0] * N for _ in range(N)]

K = int(input())
for _ in range(K):
    r, c = map(int, input().split())
    r -= 1; c -= 1
    grid[r][c] = 2
L = int(input())
command = []
for _ in range(L):
    t, d = map(str, input().split())
    t = int(t)
    command.append((t, d))

cr, cc = 0, 0
grid[cr][cc] = 1
ans = 0
k = 0
idx = 0
end = (cr, cc)
snake = deque([(0,0)])

while True:

    if idx < L and ans == command[idx][0]:
       if command[idx][1] == 'L':
           k = (k - 1) % 4
       else:
           k = (k + 1) % 4
       idx += 1

    nr, nc = cr + dr[k], cc + dc[k]
    if 0 <= nr < N and 0 <= nc < N and grid[nr][nc] != 1:
        snake.append((nr,nc))
        if grid[nr][nc] == 2:
            grid[nr][nc] = 1
        else:
            xr, xc = snake.popleft()
            grid[xr][xc] = 0
            grid[nr][nc] = 1
    else:
        ans += 1
        break

    cr, cc = nr, nc
    ans += 1

print(ans)