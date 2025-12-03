import sys; sys.stdin = open("숨바꼭질_2.txt")
from collections import deque

def go():
    global vis
    time = 0
    q = deque([me])
    vis[me] = time

    while q:
        time += 1
        for _ in range(len(q)):
            cur = q.popleft()
            for nx in (cur - 1, cur + 1, cur * 2):
                if 0 <= nx < 200000 and time < vis[nx]:
                    vis[nx] = time
                    q.append(nx)
    return

def go2():
    global min_time, cnt, vis
    q = deque([(me, 0)])

    while q:
        for _ in range(len(q)):
            cur, time = q.popleft()

            if time > min_time:
                return

            if cur == you:
                if time < min_time:
                    min_time = time
                    cnt = 1
                elif time == min_time:
                    cnt += 1
                continue

            for nx in (cur * 2, cur - 1, cur + 1):
                if 0 <= nx < 200000 and time + 1 == vis[nx]:
                    q.append((nx, time + 1))
    return

me, you = map(int, input().split())
vis = [10 ** 9] * 200000
min_time = 10 ** 9
cnt = 0
go()
go2()
print(min_time)
print(cnt)