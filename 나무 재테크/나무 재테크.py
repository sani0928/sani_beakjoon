import sys; sys.stdin = open("나무 재테크.txt")
from collections import deque

N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
# 양분 정보
grid = [[5] * N for _ in range(N)]

lst = []
dr, dc = (-1,-1,0,1,1,1,0,-1), (0,1,1,1,0,-1,-1,-1)

for _ in range(M):
    x, y, z = map(int, input().split())
    # 나이, 계절순환, r, c, 생사여부
    lst.append((z, 0, x-1, y-1, True))

lst.sort()
q = deque()

for a, t, r, c, alive in lst:
    q.append((a, t, r, c, alive))

ans = 0
stop = False
while q:

    age, time, r, c, alive = q.popleft()
    # print(f'나이: {age}, 시간: {time}, 좌표: {r}, {c}, 생존: {alive}, 나무 위치 양분: {grid[r][c]}')

    if time == K * 4 and alive:
        ans += 1

    # 봄
    elif time % 4 == 0:
        # 계절이 봄으로 바뀌면 stop 다시 False로
        if stop:
            stop = False
        if grid[r][c] >= age:
            grid[r][c] -= age
            age += 1
        else:
            alive = False
        q.append((age, time +  1, r, c, alive))

    # 여름
    elif time % 4 == 1:
        if not alive:
            grid[r][c] += age // 2
        else:
            q.append((age, time + 1, r, c, alive))

    # 가을
    elif time % 4 == 2:
        if age % 5 == 0:
            for k in range(8):
                nr, nc = r + dr[k], c + dc[k]
                if 0 <= nr < N and 0 <= nc < N:
                    q.append((1, time + 1, nr, nc, True))
            q.append((age, time + 1, r, c, alive))
        else:
            q.append((age, time + 1, r, c, alive))

    # 겨울 (로봇 작동은 한 번만)
    if time % 4 == 3:
        if not stop:
            for i in range(N):
                for j in range(N):
                    grid[i][j] += A[i][j]
                    stop = True
        q.append((age, time + 1, r, c, alive))

    # for chunk in grid:
    #     print(*chunk)
    # print('-----------------')

print(ans)