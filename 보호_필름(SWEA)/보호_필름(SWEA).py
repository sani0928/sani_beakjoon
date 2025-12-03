import sys; sys.stdin = open("보호_필름(SWEA).txt")
import copy

T = int(input())
for tc in range(1, T + 1):
    D, W, K = map(int, input().split())
    film = [list(map(int, input().split())) for _ in range(D)]
    ans = 0
    vis = [False] * D

    def count(new_film):

        for c in range(W):
            cnt = 1
            cell = new_film[0][c]
            for r in range(1, D):

                if cnt == K:
                    print(f'#{tc} {c}번째 통과')
                    break

                if new_film[r][c] == cell:
                    cnt += 1
                else:
                    cell = new_film[r][c]
                    cnt = 1

            if cnt < K:
                print(f'#{tc} {c}번째 불통과')
                return False

        return True




