import sys; sys.stdin = open("경로_찾기.txt")
from collections import deque

def hamming(a, b):
    diff = 0
    for num, num2 in zip(a, b):
        if num != num2:
            diff += 1

    return diff == 1

N, K = map(int, input().split())
codes = [[-1] * K] + [list(map(int, input())) for _ in range(N)]
s, e = map(int, input().split())
prev = [-1] * len(codes)
q = deque([s])
vis = [False] * len(codes)
vis[s] = True

while q:
    u = q.popleft()

    if u == e:
        break

    for v in range(1, len(codes)):
        if not vis[v] and hamming(codes[u], codes[v]):
            vis[v] = True
            prev[v] = u
            q.append(v)

ans = [e]
cur = e
while True:

    if prev[cur] == -1:
        break
    ans.append(prev[cur])
    cur = prev[cur]

if cur == s:
    ans.reverse()
    print(*ans)
else:
    print(-1)