import sys; sys.stdin = open("Ladder2.txt")

dr,dc = (0,0,1), (-1,1,0)
for _ in range(10):
    test_case = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    min_cnt = 10 ** 9
    ans = None
    for i in range(100):
        if ladder[0][i] == 1:
            s = [(0,i,0)]
            vis = [[False] * 100 for _ in range(100)]
            while s:
                r, c, cnt = s.pop()
                if r == 99:
                    if min_cnt > cnt:
                        min_cnt = cnt
                        ans = i
                    break

                for k in range(3):
                    nr, nc = r + dr[k], c + dc[k]
                    if 0 <= nr < 100 and 0 <= nc < 100 and ladder[nr][nc] == 1 and not vis[nr][nc]:
                        vis[nr][nc] = True
                        s.append((nr, nc, cnt+1))
                        break
    print(f'#{test_case} {ans}')