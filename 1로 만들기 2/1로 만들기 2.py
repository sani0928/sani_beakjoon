import sys; sys.stdin = open("1로 만들기 2.txt")
from collections import deque

N = int(input())
# 최단 계산 경로 추적용 (N은 부모가 없으므로 0 처리)
parent = [-1] * (N + 1)
parent[N] = 0
# 중복 계산 방지
visited = set()
visited.add(N)

q = deque()
# 현재 값, 계산 횟수
q.append((N, 0))
# 최소 계산 횟수 (임시로 -1)
ans1 = -1

while q:

    num, cnt = q.popleft()

    if num == 1:
        # 값이 1이 되면 최소 계산 횟수 챙기고 break
        ans1 = cnt
        break

    if num % 3 == 0 and num // 3 not in visited:
        visited.add(num // 3)
        next_num = num // 3
        parent[next_num] = num
        q.append((next_num, cnt + 1))

    if num % 2 == 0 and num // 2 not in visited:
        visited.add(num // 2)
        next_num = num // 2
        parent[next_num] = num
        q.append((next_num, cnt + 1))

    if num - 1 not in visited:
        visited.add(num - 1)
        next_num = num - 1
        parent[next_num] = num
        q.append((next_num, cnt + 1))

# N -> 1 최단 계산 경로 역추적
ans2 = []
start = 1

while start != N:
    ans2.append(start)
    start = parent[start]
ans2.append(N)
ans2.reverse()

ans.append(ans1)
ans.append(*ans2)
