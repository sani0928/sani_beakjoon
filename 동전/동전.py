import sys; sys.stdin = open("동전.txt")

T = int(input())
for _ in range(T):
    N = int(input())
    coins = list(map(int, input().split()))
    coins.sort(reverse=True)
    M = int(input())
    print(coins)