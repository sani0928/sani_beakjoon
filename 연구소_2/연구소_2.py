import sys; sys.stdin = open("연구소_2.txt")
from collections import deque
from itertools import combinations

dr, dc = (0,1,0,-1), (1,0,-1,0)
def bfs(lst1, blank_cnt):
    global ans

    left_blank = blank_cnt
    q = deque()
    vis = [[False] * N for _ in range(N)]
    for r, c in lst1:
        q.append((r, c))
        vis[r][c] = True
    time = 0

    while q:
        for _ in range(len(q)):
            cr, cc = q.popleft()
            for k in range(4):
                nr, nc = cr + dr[k], cc + dc[k]
                if 0 <= nr < N and 0 <= nc < N and not vis[nr][nc]:
                    if grid[nr][nc] != 1:
                        left_blank -= 1
                        vis[nr][nc] = True
                        q.append((nr, nc))
        time += 1

    if left_blank != 0:
        return
    ans = min(ans, time - 1)
    return

def coordinate():
    coors = set()
    for r in range(N):
        for c in range(N):
            if grid[r][c] == 2:
                coors.add((r,c))
    return coors

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
ans = 50*50
lst = coordinate()
blank = (N*N) - M
for r in range(N):
    for c in range(N):
        if grid[r][c] == 1:
            blank -= 1
for br in combinations(lst, M):
    bfs(br, blank)
print(ans if ans != 50*50 else -1)