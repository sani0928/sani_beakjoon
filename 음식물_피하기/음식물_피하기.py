import sys; sys.stdin = open("음식물_피하기.txt")
from collections import deque

def start(sr, sc):
    global vis

    q = deque([(sr, sc)])
    vis[sr][sc] = True
    cnt = 1

    while q:

        cr, cc = q.popleft()
        for k in range(4):
            nr, nc = cr + dr[k], cc + dc[k]
            if 0 <= nr < N and 0 <= nc < M:
                if not vis[nr][nc] and matrix[nr][nc] == 1:
                    cnt += 1
                    vis[nr][nc] = True
                    q.append((nr, nc))
    return cnt

dr, dc = (0,1,0,-1), (1,0,-1,0)
N, M, K = map(int, input().split())
matrix = [[0] * M for _ in range(N)]
vis = [[False] * M for _ in range(N)]
ans = 0

for _ in range(K):
    r, c = map(int, input().split())
    r, c = r - 1, c - 1
    matrix[r][c] = 1

for r in range(N):
    for c in range(M):
        if matrix[r][c] and not vis[r][c]:
            ans = max(ans, start(r, c))
print(ans)