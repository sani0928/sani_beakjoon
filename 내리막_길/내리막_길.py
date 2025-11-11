import sys; sys.stdin = open("내리막_길.txt")

dr, dc = (0,1,0,-1), (1,0,-1,0)
ans = 0
M, N = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(M)]
vis = [[False] * N for _ in range(M)]

for r in range(M):
    for c in range(N):
        if grid[0][0] < grid[r][c] or grid[M-1][N-1] > grid[r][c]:
            vis[r][c] = True

s = [(0, 0)]
vis[0][0] = True
while s:
    r, c = s.pop()

    if r == M - 1 and c == N - 1:
        ans += 1

    for k in range(4):
        nr, nc = r + dr[k], c + dc[k]
        if 0 <= nr < M and 0 <= nc < N and not vis[nr][nc]:
            if grid[nr][nc] < grid[r][c]:
                s.append((nr, nc))

print(ans)