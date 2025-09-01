import sys; sys.stdin = open("패션왕 신해빈.txt")

T = int(input())

for _ in range(T):

    N = int(input())
    have = []
    for _ in range(N):
        name, category = map(str, input().split())
        have.append((name, category))
    cnt = 0

