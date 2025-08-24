import sys; sys.stdin = open("input.txt")
import heapq

N, M = map(int, input().split())
grid = [list(map(int, input().strip())) for _ in range(M)]
cnt_map = [[float('inf')] * N for _ in range(M)]

start_r, start_c = 0, 0
goal_r, goal_c = M - 1, N - 1
dr, dc = (0, 1, 0, -1), (1, 0, -1, 0)

cnt_map[start_r][start_c] = 0
pq = [(0, start_r, start_c)]

while pq:

    cnt, cr, cc = heapq.heappop(pq)

    if cnt < cnt_map[cr][cc]:
        continue

    if cr == goal_r and cc == goal_c:
        break

    for k in range(4):
        nr, nc = cr + dr[k], cc + dc[k]
        if 0 <= nr < M and 0 <= nc < N:
            ncnt = cnt + grid[nr][nc]
            if ncnt < cnt_map[nr][nc]:
                cnt_map[nr][nc] = ncnt
                heapq.heappush(pq, (ncnt, nr, nc))

ans.append(cnt_map[M - 1][N - 1])

