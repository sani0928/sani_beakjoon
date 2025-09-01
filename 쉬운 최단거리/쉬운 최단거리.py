import sys; sys.stdin = open("쉬운 최단거리.txt")
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

def searching_goal():
    for r in range(N):
        for c in range(M):
            if matrix[r][c] == 2:
                return r, c
INF = 100**9
dist = [[-1] * M for _ in range(N)]
dr, dc = (0, 1, 0, -1), (1, 0, -1, 0)
goal_r, goal_c = searching_goal()
dist[goal_r][goal_c] = 0

q = deque([(goal_r,goal_c)])

while q:

    r, c = q.popleft()

    for k in range(4):
        nr, nc = r + dr[k], c + dc[k]
        if 0 <= nr < N and 0 <= nc < M:
            if matrix[nr][nc] != 0:
                if dist[nr][nc] == -1:
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr,nc))

for i in range(N):
    row = []
    for j in range(M):
        if matrix[i][j] == 0:
            row.append(0)
        else:
            row.append(dist[i][j])
    print(*row)