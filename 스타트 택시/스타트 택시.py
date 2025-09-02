import sys; sys.stdin = open("스타트 택시.txt")
from collections import deque

def to_destination(r, c, num, g):
    global grid, cnt

    q = deque()
    q.append((r, c, num, g))

    while q:

        r, c, num, g = q.popleft()
        print(f'태운 손님: {num}, 남은 가스 : {g}')

        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if 0 <= nr < N and 0 <= nc < N and grid[nr][nc] != 1:
                if grid[nr][nc] != 0:
                    same, var = grid[nr][nc]
                    if same == num and var == 'end':
                        g -= 1
                        g = g * 2
                        cnt += 1
                        print(f'손님{num} 내림, 남은 가스: {g}')
                        return nr, nc, g
                else:
                    g -= 1
                    q.append((nr, nc, num, g))

N, M, G = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
sr, sc = map(int, input().split())
sr -= 1; sc -= 1

dr, dc = (-1, 0, 1, 0), (0, -1, 0, 1)
dist = [[float('inf')] * N for _ in range(N)]
dist[sr][sc] = 0
cnt = 0
used = []
for num in range(1, M + 1):
    r, c, er, ec = map(int, input().split())
    grid[r-1][c-1] = (num, 'start')
    grid[er-1][ec-1] = (num, 'end')

for chunk in grid:
    print(*chunk)


q = deque()
q.append((sr, sc, G))
visited = [[False] * N for _ in range(N)]
visited[sr][sc] = True

while q:

    r, c, g = q.popleft()

    if cnt == M:
        print('끝')
        break

    if g == 0:
        print(-1)
        break

    for k in range(4):
        nr, nc = r + dr[k], c + dc[k]
        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and grid[nr][nc] != 1:
            if grid[nr][nc] != 0:
                visited[nr][nc] = True
                num, var = grid[nr][nc]
                if not num in used and var == 'start':
                    g -= 1
                    print(f'손님 {num} 막 태움, 남은 가스: {g}, 좌표({nr + 1}, {nc + 1})')
                    used.append(num)
                    q = deque()
                    nr, nc, g = to_destination(nr, nc, num, g)
                    q.append((nr, nc, g))
                else:
                    print(f'손님 없음(도착지 위치), 남은 가스: {g}, 좌표({nr + 1}, {nc + 1})')
                    g -= 1
                    q.append((nr, nc, g))

            else:
                visited[nr][nc] = True
                g -= 1
                print(f'손님 없음, 남은 가스: {g}, 좌표({nr + 1}, {nc + 1})')
                q.append((nr, nc, g))

print(used)