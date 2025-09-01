import sys; sys.stdin = open("보물.txt")
import heapq
N = int(input())
A = list(map(int, input().split()))
B = []

for num in list((map(int, input().split()))):
    heapq.heappush(B, num)

A.sort(reverse=True)
min_value = 0

for i in range(N):
    min_value += A[i] * heapq.heappop(B)

print(min_value)

