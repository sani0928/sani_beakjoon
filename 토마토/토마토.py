import sys; sys.stdin = open("토마토.txt")
from collections import deque


# 모든 토마토 익는 시간 출력 / 모두 익어있으면 0 / 모두 익을 수 없으면 -1
# [층][행][열]
M, N, H = map(int, input().split())
boxs = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
ans = 0
# 동남서북위아래
dr, dc = (0,1,0,-1,1,-1),(1,0,-1,0)

q = deque()
vis = [[[False] * M for _ in range(N)] for _ in range(H)]

def first():

    cnt = 0
    for h in range(H):
        for r in range(N):
            for c in range(M):
                if boxs[h][r][c] == 1:
                    q.append((h, r, c))
                    vis[h][r][c] = True
                elif boxs[h][r][c] == 0:
                    cnt += 1
    # 다 익어있으면 0 출력 후 연산 종료
    if cnt == 0:
        print(0)
        sys.exit(0)
# 모두 익지 못하는 상황인지 확인
def check():
    global ans

    for h in range(H):
        for r in range(N):
            for c in range(M):
                if boxs[h][r][c] == 0:
                    ans = -1
                    return

first()

while True:

    cnt = 0
    for _ in range(len(q)):
        ch, cr, cc = q.popleft()
        for k in range(6):
            if k > 3:
                nh, nr, nc = ch + dr[k], cr, cc
            else:
                nh, nr, nc = ch, cr + dr[k], cc + dc[k]
            if 0 <= nh < H and 0 <= nr < N and 0 <= nc < M and not vis[nh][nr][nc]:
                # 익지 않은 토마토
                if boxs[nh][nr][nc] == 0:
                    vis[nh][nr][nc] = True
                    boxs[nh][nr][nc] = 1
                    cnt += 1
                    q.append((nh, nr, nc))
    if cnt == 0:
        check()
        break
    ans += 1

time = ans
print(time)
