import sys; sys.stdin = open("벽 부수고 이동하기 3.txt")
from collections import deque

input = sys.stdin.readline
N, M, K = map(int, input().split())
grid = [list(map(int, input())) for _ in range(N)]
visited = [[[0] * (K+1) for _ in range(M)] for _ in range(N)]
visited[0][0][K] = 1
# 가만히, 우하좌상
dr, dc = (0,1,0,-1), (1,0,-1,0)
# 좌표, 뿌수기 횟수, 거리, 시간
q = deque([(0,0,K,1,1)])

while q:

    r, c, k, dist, time = q.popleft()

    if r == N - 1 and c == M - 1:
        print(dist)
        sys.exit(0)

    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if 0 <= nr < N and 0 <= nc < M and visited[nr][nc][k] == 0:
            nk = k - grid[nr][nc]
            # 앞에 벽이 있으면
            if k != nk:
                if nk >= 0:
                    # 낮이면
                    if time == 1:
                        visited[nr][nc][nk] = 1
                        q.append((nr,nc,nk,dist+1,1-time))
                    else:
                        visited[nr][nc][nk] = 1
                        q.append((r,c,k,dist+1,1-time))
            else:
                visited[nr][nc][nk] = 1
                q.append((nr,nc,nk,dist+1,1-time))
print(-1)