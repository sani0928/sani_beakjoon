import sys; sys.stdin = open("N번째 큰 수.txt")
import heapq

N = int(input())

matrix = [list(map(int, input().split())) for _ in range(N)]

q = []

for r in range(N):
    for c in range(N):
        heapq.heappush(q, -matrix[r][c])
        ans.append(q)

for _ in range(N-1):
    heapq.heappop(q)

ans.append(-1 * heapq.heappop(q))