import sys; sys.stdin = open("보급로(SWEA).txt")
from collections import deque
input = sys.stdin.readline
dr, dc = (0,1,0,-1), (1,0,-1,0)
T = int(input())
for tc in range(1, T + 1):
    ans = 10**9
    N = int(input())
    grid = [list(map(int, input().strip())) for _ in range(N)]
    q = deque([(0,0,0)])
    vis = [[float('inf')] * N for _ in range(N)]

    while q:

        r, c, cost = q.popleft()
        if r == N - 1 and c == N - 1:
            ans = min(ans, cost)

        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if 0 <= nr < N and 0 <= nc < N:
                next_cost = cost + grid[nr][nc]
                if vis[nr][nc] > next_cost:
                    vis[nr][nc] = next_cost
                    q.append((nr,nc,next_cost))

    print(f'#{tc} {ans}')