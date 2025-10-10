import sys; sys.stdin = open("벽 부수고 이동하기 2.txt")
from collections import deque

N, M, K = map(int, input().split())
grid = [list(map(int, input())) for _ in range(N)]
dr, dc = (0,1,0,-1), (1,0,-1,0)
visited = [[[0] * (K + 1) for _ in range(M)] for _ in range(N)]
visited[0][0][K] = True
# 시작 위치, 남은 부수기 횟수, 거리
q = deque([(0,0,K,1)])

def go():
    while q:

        r, c, k, dist = q.popleft()

        if r == N - 1 and c == M - 1:
            return dist

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < N and 0 <= nc < M:
                if grid[nr][nc] == 0:
                    if visited[nr][nc][k] == 0:
                        visited[nr][nc][k] = 1
                        q.append((nr, nc, k, dist + 1))
                else:
                    nk = k - grid[nr][nc]
                    if nk >= 0 and visited[nr][nc][nk] == 0:
                        visited[nr][nc][nk] = 1
                        q.append((nr, nc, nk, dist + 1))

    return -1

print(go())