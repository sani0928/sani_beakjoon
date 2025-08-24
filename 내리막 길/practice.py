import sys; sys.stdin = open("input.txt")
N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

dr, dc = (1, -1, 0, 0), (0, 0, 1, -1)

# -1: 미계산, 그 외: 경로 수
dp = [[-1] * M for _ in range(N)]

def dfs(r, c):
    # 도착지면 경로 1개
    if r == N - 1 and c == M - 1:
        return 1
    if dp[r][c] != -1:
        return dp[r][c]

    ways = 0
    h = grid[r][c]
    for k in range(4):
        nr, nc = r + dr[k], c + dc[k]
        if 0 <= nr < N and 0 <= nc < M and grid[nr][nc] < h:
            ways += dfs(nr, nc)

    dp[r][c] = ways
    return ways


ans.append(dfs(0, 0))
for c in dp:
    ans.append(*c)