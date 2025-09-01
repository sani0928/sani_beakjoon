import sys; sys.stdin = open("불!.txt")
from collections import deque
R, C = map(int, input().split())
grid = [list(map(str, input().strip())) for _ in range(R)]

visited = [[False] * C for _ in range(R)]
dist = [[float('inf')] * C for _ in range(R)]

dr, dc = (0, 1, 0, -1), (1, 0, -1, 0)

me_q = deque()
fire_q = deque()

for r in range(R):
    for c in range(C):
        if grid[r][c] == 'F':
            dist[r][c] = 0
            fire_q.append((r, c))
        elif grid[r][c] == 'J':
            me_q.append((r, c))

# 불 최단거리 계산
while fire_q:

    fire_r, fire_c = fire_q.popleft()

    for k in range(4):
        fire_nr, fire_nc = fire_r + dr[k], fire_c + dc[k]
        if 0 <= fire_nr < R and 0 <= fire_nc < C and grid[fire_nr][fire_nc] != '#':
            if dist[fire_r][fire_c] + 1 < dist[fire_nr][fire_nc]:
                dist[fire_nr][fire_nc] = dist[fire_r][fire_c] + 1
                fire_q.append((fire_nr, fire_nc))

for chunk in dist:
    print(*chunk)

def go():
    time = 0
    # me 이동
    while me_q:

        time += 1
        for _ in range(len(me_q)):
            me_r, me_c = me_q.popleft()
            if me_r == 0 or me_r == R - 1 or me_c == 0 or me_c == C - 1:
                return time
            for k in range(4):
                me_nr, me_nc = me_r + dr[k], me_c + dc[k]
                if 0 <= me_nr < R and 0 <= me_nc < C and grid[me_nr][me_nc] == '.':
                    # 실제 타임이 해당 위치 불 최단거리보다 작다면
                    if not visited[me_nr][me_nc] and dist[me_nr][me_nc] > time:
                        visited[me_nr][me_nc] = True
                        me_q.append((me_nr, me_nc))

    return 'IMPOSSIBLE'

print(go())