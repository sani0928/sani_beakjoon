import sys; sys.stdin = open("숨바꼭질_5.txt")
from collections import deque

def go():
    global vis

    time = 0
    q = deque([N])
    vis[N] = 0

    while q:

        for _ in range(len(q)):
            cur = q.popleft()
            for nx in (cur - 1, cur + 1, cur * 2):
                if 0 <= nx < MAX and time < vis[nx]:
                    vis[nx] = time + 1
                    q.append(nx)
        time += 1

    return

def go2():
    global vis

    plus = 0
    time = 0
    goal = K
    q = deque([N])

    while q:
        plus += 1

        if goal > 500000:
            return -1

        for _ in range(len(q)):
            cur = q.popleft()

            if cur == goal:
                print(cur)
                return vis[cur]

            for nx in (cur - 1, cur + 1, cur * 2):
                if 0 <= nx < MAX:
                    if time <= vis[nx]:
                        q.append(nx)
                    else:
                        vis[nx] = time + 1
        time += 1
        goal += plus

    return -1


N, K = map(int, input().split())
MAX = 500001
vis = [10**9] * MAX
go()
print(go2())
