import sys; sys.stdin = open("욕심쟁이_판다.txt")
dr, dc = (0,1,0,-1), (1,0,-1,0)
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

ans = 0


def dfs(cr, cc):
    global dp

    if dp[cr][cc] != -1:
        return dp[cr][cc]

    dp[cr][cc] = 0
    cnt = 4
    for k in range(4):
        nr, nc = cr + dr[k], cc + dc[k]
        if 0 <= nr < N and 0 <= nc < N:
            if board[nr][nc] > board[cr][cc]:
                dp[cr][cc] += dfs(nr, nc)
            else:
                cnt -= 1
        else:
            cnt -= 1
    if cnt == 0:
        return 1
    for ch in dp:
        print(*ch)
    return dp[cr][cc]


for r in range(N):
    for c in range(N):
        dp = [[-1] * N for _ in range(N)]
        print(dfs(r, c))