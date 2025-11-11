import sys; sys.stdin = open("점프.txt")

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]

def go(r, c):

    if r == N - 1 and c == N - 1:
        dp[r][c] += 1
        print('end')
        return

    if r < N and c < N:
        nr = grid[r][c]
        nc = grid[r][c]
        dp[nr][c] += 1
        dp[r][nc] += 1
        go(nr, c)
        go(r, nr)
    return

go(0, 0)
print(dp[N-1][N-1])