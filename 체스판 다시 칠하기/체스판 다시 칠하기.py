import sys; sys.stdin = open("체스판 다시 칠하기.txt")

N, M = map(int, input().split())

chess_map = [list(input().strip()) for _ in range(N)]

ans = 64

# 8x8 격차로 전체 검색
for i in range(N - 8 + 1):
    # 0 나오면 더 이상 연산 불필요
    if ans == 0:
        break
    for j in range(M - 8 + 1):
        # 틀린 판 갯수 체크
        cntB = 0
        cntW = 0
        for r in range(i, i + 8):
            # 맨 왼쪽 위가 B로 시작하는 체스판으로 만들 때
            for c in range(j, j + 8):
                if (r-i) % 2 == 0:
                    if 'B' if (c-j) & 2 == 0 else 'W' != chess_map[r][c]:
                        cntB += 1

                    if 'W' if (c-j) & 2 == 0 else 'B' != chess_map[r][c]:
                        cntW += 1
                else:
                    if 'W' if (c-j) & 2 == 0 else 'B' != chess_map[r][c]:
                        cntB += 1

                    if 'B' if (c-j) & 2 == 0 else 'W' != chess_map[r][c]:
                        cntW += 1

        print(f'cntB: {cntB}, cntW: {cntW}')
        ans = min(ans, cntB, cntW)
        print(ans)

print(ans)
