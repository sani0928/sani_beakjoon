import sys; sys.stdin = open("숨바꼭질_2.txt")
from collections import deque

me, you = map(int, input().split())
q = deque([(0, me)])
ans = 10**9
cnt = 0

vis = [False] * 100001
vis[me] = True

while q:

    time, cur = q.popleft()

    if time > ans:
        continue

    if cur == you and time <= ans:
        ans = time
        cnt += 1
        continue

    for nx in (cur - 1, cur + 1, cur * 2):
        if 0 <= nx <= 100000 and not vis[nx]:
            vis[nx] = True
            q.append((time + 1, nx))

print(ans)
print(cnt)