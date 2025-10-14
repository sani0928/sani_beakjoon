import sys; sys.stdin = open("다리_만들기.txt")
from collections import deque

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
dr, dc = (0,1,0,-1), (1,0,-1,0)
ans = 10**9
cnt = 1
save = set()

def classify(sr, sc):
    global cnt

    q = deque([(sr, sc)])
    visited = [[False] * N for _ in range(N)]
    visited[sr][sc] = True
    grid[sr][sc] = cnt

    while q:

        cr, cc = q.popleft()
        for k in range(4):
            nr, nc = cr + dr[k], cc + dc[k]
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                if grid[nr][nc] == 1:
                    visited[nr][nc] = True
                    grid[nr][nc] = cnt
                    q.append((nr, nc))
                else:
                    # 해안선 저장
                    save.add((cr, cc))



    cnt += 1
    return

def searching(sr, sc, bf):
    global ans

    q = deque([(sr, sc, 0)])
    visited = [[False] * N for _ in range(N)]
    visited[sr][sc] = True

    while q:

        cr, cc, length = q.popleft()
        for k in range(4):
            nr, nc = cr + dr[k], cc + dc[k]
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                if grid[nr][nc] == 0:
                    visited[nr][nc] = True
                    q.append((nr, nc, length + 1))
                elif grid[nr][nc] != bf:
                    ans = min(ans, length)
                    return
    return

for r in range(N):
    for c in range(N):
        if grid[r][c] == 1:
            classify(r, c)

for r2, c2 in save:
    before = grid[r2][c2]
    searching(r2, c2, before)

print(ans)