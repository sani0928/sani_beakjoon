import sys; sys.stdin = open("회전하는 큐.txt")
from collections import deque

N, M = map(int, input().split())

q = deque()

for i in range(1,N + 1):
    q.append('a' + str(i))

print(q)
