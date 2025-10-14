import sys; sys.stdin = open("RGB거리.txt")

# 빨초파
N = int(input())
r, g, b = map(int, input().split())

for i in range(1, N):
    nr, ng, nb = map(int, input().split())
    r, g, b = min(g, b) + nr, min(r, b) + ng, min(r, g) + nb

print(min(r, g, b))