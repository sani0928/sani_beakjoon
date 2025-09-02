import sys; sys.stdin = open("경쟁적 전염.txt")
import heapq

N, K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())

dr, dc = (0,1,0,-1), (1,0,-1,0)
lst = []
pq = []

for i in range(N):
    for j in range(N):
        if grid[i][j] != 0:
            lst.append((0, grid[i][j], i, j))

lst.sort()

for t, n, r, c in lst:
    heapq.heappush(pq, (t,n,r,c))

while pq:

    time, num, r, c = heapq.heappop(pq)

    if time == S:
        break

    for k in range(4):
        nr, nc = r + dr[k], c + dc[k]
        if 0 <= nr < N and 0 <= nc < N and grid[nr][nc] == 0:
            grid[nr][nc] = num
            heapq.heappush(pq, (time + 1, num, nr, nc))

    # for chunk in grid:
    #     print(chunk)
    # print('---------------')

print(grid[X-1][Y-1])

