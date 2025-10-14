import sys; sys.stdin = open("로봇.txt")
from collections import deque
# 동1,서2,남3,북4
N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
sr, sc, sdir = map(int, input().split())
er, ec, edir = map(int, input().split())
sr, sc, er, ec = sr - 1, sc - 1, er - 1, ec - 1
# 동서남북 순서
dr, dc = (0,0,1,-1), (1,-1,0,0)

# 행, 열, 방향, 명령수
q = deque([(sr, sc, sdir, 0)])
vis = [[[False] * 5 for _ in range(M)] for _ in range(N)]
vis[sr][sc][sdir] = True

while q:

    cr, cc, dir, cnt = q.popleft()
    # print(cr, cc, dir, cnt)
    if cr == er and cc == ec and dir == edir:
        print(cnt)
        break

    # Turn 명령
    if dir == 1 or dir == 2:
        for i in range(3, 5):
            ndir = i
            if not vis[cr][cc][ndir]:
                vis[cr][cc][ndir] = True
                q.append((cr, cc, ndir, cnt + 1))
    else:
        for i in range(1, 3):
            ndir = i
            if not vis[cr][cc][ndir]:
                vis[cr][cc][ndir] = True
                q.append((cr, cc, ndir, cnt + 1))
    # Go 명령
    if dir == 1:
        for k in range(1, 4):
            nc = cc + dc[0]*k
            if nc < M and not vis[cr][nc][dir]:
                if grid[cr][nc] != 1:
                    vis[cr][nc][dir] = True
                    # print(f'{dir}로 {k}칸 이동: {cr} {nc} {cnt + 1}')
                    q.append((cr, nc, dir, cnt + 1))
                else:
                    break
    elif dir == 2:
        for k in range(1, 4):
            nc = cc + dc[1]*k

            if 0 <= nc and not vis[cr][nc][dir]:
                if grid[cr][nc] != 1:
                    vis[cr][nc][dir] = True
                    # print(f'{dir}로 {k}칸 이동: {cr} {nc} {cnt + 1}')
                    q.append((cr, nc, dir, cnt + 1))
                else:
                    break
    elif dir == 3:
        for k in range(1, 4):
            nr = cr + dr[2]*k
            if nr < N and not vis[nr][cc][dir]:
                if grid[nr][cc] != 1:
                    vis[nr][cc][dir] = True
                    # print(f'{dir}로 {k}칸 이동: {nr} {cc} {cnt + 1}')
                    q.append((nr, cc, dir, cnt + 1))
                else:
                    break
    elif dir == 4:
        for k in range(1, 4):
            nr = cr + dr[3]*k

            if 0 <= nr and not vis[nr][cc][dir]:
                if grid[nr][cc] != 1:
                    vis[nr][cc][dir] = True
                    # print(f'{dir}로 {k}칸 이동: {nr} {cc} {cnt + 1}')
                    q.append((nr, cc, dir, cnt + 1))
                else:
                    break