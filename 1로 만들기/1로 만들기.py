import sys; sys.stdin = open("1로 만들기.txt")
from collections import deque

N = int(input())

visited = set()
visited.add(N)

q = deque()
q.append((N, 0))

while q:

    num, cnt = q.popleft()

    if num == 1:
        ans.append(cnt)
        break

    if num % 3 == 0 and num // 3 not in visited:
        next_num = num // 3
        visited.add(next_num)
        q.append((next_num, cnt + 1))

    if num % 2 == 0 and num // 2 not in visited:
        next_num = num // 2
        visited.add(next_num)
        q.append((next_num, cnt + 1))

    if num - 1 not in visited:
        next_num = num - 1
        visited.add(next_num)
        q.append((next_num, cnt + 1))