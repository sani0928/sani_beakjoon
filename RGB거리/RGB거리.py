import sys; sys.stdin = open("RGB거리.txt")

N = int(input())

grid = [list(map(int, input().split())) for _ in range(N)]

def go(subset, R, G, B, turn):

    if turn == N - 1:
        return subset

    if R:
        R = False
        go(subset + [grid[turn][1]], R, G, B, turn + 1)
        go(subset + [grid[turn][2]], R, G, B, turn + 1)
        R = True

    if G:
        G = False
        go(subset + [grid[turn][0]], R, G, B, turn + 1)
        go(subset + [grid[turn][2]], R, G, B, turn + 1)
        G = True

    if B:
        B = False
        go(subset + [grid[turn][0]], R, G, B, turn + 1)
        go(subset + [grid[turn][1]], R, G, B, turn + 1)
        B = True


ans.append(go([], True, True, True, 0))