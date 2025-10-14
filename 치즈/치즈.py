import sys; sys.stdin = open("치즈.txt")
from collections import deque
# 매번 바깥 공기 순환하면서 겉 치즈 조사
# 그 후 한번에 녹이기 (남은 치즈 갯수 조사)
# 남은 치즈가 하나도 없다면 현재 시간과 이전 남은 치즈 갯수 출력

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
dr, dc = (0,1,0,-1), (1,0,-1,0)
time, cnt = 0, 0
cheeze = []

def checking():
    global cheeze

    q = deque([(0,0)])
    visited = [[False] * M for _ in range(N)]
    visited[0][0] = True

    while q:

        cr, cc = q.popleft()
        for k in range(4):
            nr, nc = cr + dr[k], cc + dc[k]
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                if grid[nr][nc] == 1:
                    cheeze.append((nr,nc))
                    visited[nr][nc] = True
                else:
                    q.append((nr,nc))
                    visited[nr][nc] = True
    return

def melting():
    global cheeze

    if not cheeze:
        return 0

    while cheeze:

        r, c = cheeze.pop()
        grid[r][c] = 0

    return 1

while True:

    checking()
    temp = 0
    for r in range(N):
        for c in range(M):
            if grid[r][c] == 1:
                temp += 1
    if temp != 0:
        cnt = temp

    if melting() == 1:
        time += 1
    else:
        print(time)
        print(cnt)
        break