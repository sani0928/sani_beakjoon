import sys; sys.stdin = open("1, 2, 3 더하기.txt")

T = int(input())

for _ in range(T):
    num = int(input())
    dp = [[False] for _ in range(num + 1)]
    print(dp)