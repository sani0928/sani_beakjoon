import sys; sys.stdin = open("미세먼지_안녕!.txt")

N, M, T = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
dr, dc = (0,1,0,-1), (1,0,-1,0)
time = 0
def searching():
    u, d = (), ()
    for r in range(N):
        if grid[r][0] == -1:
            u = (r,0)
            d = (r+1,0)
            break
    return u, d

# dust = [(r,c,농도)]
def check_dust():
    dust = []
    for r in range(N):
        for c in range(M):
            if grid[r][c] != 0 and grid[r][c] != -1:
                dust.append((r,c,grid[r][c]))
    return dust

def spread(dust):

    for r, c, num in dust:
        cnt = 0
        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if 0 <= nr < N and 0 <= nc < M:
                if grid[nr][nc] != -1:
                    cnt += 1
                    grid[nr][nc] += num//5

        if num - (grid[r][c]//5)*cnt >= 0:
            grid[r][c] -= (num//5)*cnt
        else:
            grid[r][c] = 0
    return

def wind(u, d):

    ucnt = (N-1)*2 + u[0]*2
    dcnt = (N-1)*2 + (M-1-d[0])*2

    ur, uc = u; dr, dc = d
    grid[ur-1][uc] = 0; grid[dr+1][uc] = 0


(2,1) (2,2) (1,2) (0,2) (0,1) (0,0) (0,1) (0,2)
up, down = searching()
print(up, down)
print('test', 43//5)
while time != T:
    dust = check_dust()
    print(dust)
    spread(dust)


    for chunk in grid:
        print(*chunk)

    time +=1