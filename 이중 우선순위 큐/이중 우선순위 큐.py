import sys; sys.stdin = open("이중 우선순위 큐.txt")
import heapq


T = int(input())
for _ in range(T):

    Q = []
    N = int(input())
    for _ in range(N):
        cmd, num = input().split()
        num = int(num)
        if cmd == 'I':
            if num < 0:
                heapq.heappush(Q, num)
            else:
                heapq.heappush(Q, -num)
        elif cmd == 'D':
            if num == -1:
                heapq.heappop(Q)
            else:


    if Q:

    else:
        print('EMPTY')

