import sys; sys.stdin = open("구간 합 구하기 5.txt")
from collections import deque

input = sys.stdin.readline
# N, M = map(int, input().split())

# matrix = [list(map(int, input().split())) for _ in range(N)]
#
# ps = [[0]*(N+1) for _ in range(N+1)]
# for i in range(1, N+1):
#     row = matrix[i-1]
#     for j in range(1, N+1):
#         ps[i][j] = row[j-1] + ps[i-1][j] + ps[i][j-1] - ps[i-1][j-1]
# for cc in ps:
#     print(*cc)
#
# for _ in range(M):
#     r1, c1, r2, c2 = map(int, input().split())
#     print(ps[r2][c2])

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

for _ in range(M):

    x1, y1, x2, y2 = map(int, input().split())
    ans = 0
    cnt = (x2 - x1 + 1) * (y2 - y1 + 1)
