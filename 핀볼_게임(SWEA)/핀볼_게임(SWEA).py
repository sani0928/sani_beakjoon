import sys; sys.stdin = open("핀볼_게임(SWEA).txt")

dr, dc = (0,1,0,-1), (1,0,-1,0)
T = int(input())

for tc in range(1, T + 1):

    def go(cr, cc, k):

        temp = 0
        sr, sc = cr, cc
        while True:

            cr, cc = cr + dr[k], cc + dc[k]
            if 0 > cr or N <= cr or 0 > cc or N <= cc:
                temp += 1
                k = (k + 2) % 4
                continue

            # 시작 위치로 되돌
            if (cr, cc) == (sr, sc):
                return temp

            nx = grid[cr][cc]

            if nx == -1:
                return temp

            elif nx == 0:
                continue

            elif 1 <= nx <= 5:

                temp += 1
                if nx == 1:
                    if k == 0:
                        k = (k + 2) % 4
                    elif k == 1:
                        k = (k - 1) % 4
                    elif k == 2:
                        k = (k + 1) % 4
                    else:
                        k = (k + 2) % 4

                elif nx == 2:
                    if k == 0:
                        k = (k + 2) % 4
                    elif k == 1:
                        k = (k + 2) % 4
                    elif k == 2:
                        k = (k - 1) % 4
                    else:
                        k = (k + 1) % 4

                elif nx == 3:
                    if k == 0:
                        k = (k + 1) % 4
                    elif k == 1:
                        k = (k + 2) % 4
                    elif k == 2:
                        k = (k + 2) % 4
                    else:
                        k = (k - 1) % 4

                elif nx == 4:
                    if k == 0:
                        k = (k - 1) % 4
                    elif k == 1:
                        k = (k + 1) % 4
                    elif k == 2:
                        k = (k + 2) % 4
                    else:
                        k = (k + 2) % 4
                # nx == 5
                else:
                    k = (k + 2) % 4
                continue

            elif 6 <= nx <= 10:
                for r in range(N):
                    for c in range(N):
                        if (r != cr or c != cc) and grid[r][c] == nx:
                            cr, cc = r, c
                            break
                    else:
                        continue
                    break

    score = 0
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 0:
                for d in range(4):
                    score = max(score, go(i, j, d))

    print(f'#{tc} {score}')