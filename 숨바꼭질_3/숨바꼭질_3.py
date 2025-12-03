import sys; sys.stdin = open("숨바꼭질_3.txt")
from collections import deque

def go():
    global vis
    time = 0
    q = deque([(me, time)])
    vis[me] = time

    while q:
        for _ in range(len(q)):
            cur, time = q.popleft()
            for nx in (cur - 1, cur + 1, cur * 2):
                if 0 <= nx < 200000 and time < vis[nx]:

                    if nx == cur * 2:
                        vis[nx] = time
                        q.append((nx, time))
                    else:
                        vis[nx] = time + 1
                        q.append((nx, time + 1))
    print(vis)
    return

me, you = map(int, input().split())
vis = [10 ** 9] * 200000
ans = 10**9
go()
print(vis[you])