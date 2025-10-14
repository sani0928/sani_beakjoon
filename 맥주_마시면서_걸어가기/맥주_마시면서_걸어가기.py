import sys; sys.stdin = open("맥주_마시면서_걸어가기.txt")
from collections import deque
T = int(input())
for _ in range(T):
    N = int(input())
    cx, cy = map(int, input().split())

    stores = []
    for _ in range(N):
        x, y = map(int, input().split())
        dist = (abs(cx-x) + abs(cy-y)) // 1000
        stores.append((x, y))

    rock_x, rock_y = map(int, input().split())
    print(stores)