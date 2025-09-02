import sys; sys.stdin = open("점프.txt")

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
cnt = 0

def go(r, c, jump):
    global cnt

    if grid[r][c] == 0:
        cnt += 1
        return

    if r + jump < N:
        nr = r + jump
        go(nr, c, grid[nr][c])

    if c + jump < N:
        nc = c + jump
        go(r, nc, grid[r][nc])

    return

go(0,0,grid[0][0])
print(cnt)