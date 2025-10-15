import sys; sys.stdin = open("맥주_마시면서_걸어가기.txt")
from collections import deque

def calculator(a, b):
    return True if abs(a) + abs(b) <= 1000 else False

T = int(input())
for t in range(1,T+1):
    N = int(input())
    sx, sy = map(int, input().split())
    q = deque()
    nt = deque()

    for _ in range(N):
        x, y = map(int, input().split())
        if calculator(sx - x, sy - y):
            q.append((x, y))
        else:
            nt.append((x, y))
    ex, ey = map(int, input().split())

    if calculator(sx - ex, sy - ey):
        print('happy')
        continue

    arrived = False
    while q:
        cx, cy = q.popleft()
        if calculator(cx - ex, cy - ey):
            arrived = True
            break
        for _ in range(len(nt)):
            nx, ny = nt.popleft()
            if calculator(cx - nx, cy - ny):
                q.append((nx, ny))
            else:
                nt.append((nx, ny))

    print('happy' if arrived else 'sad')