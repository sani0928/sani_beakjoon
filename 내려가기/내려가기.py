import sys; sys.stdin = open("내려가기.txt")


N = int(input())

a, b, c = list(map(int, input().split()))

minium = [a, b, c]
maxium = [a, b, c]

for i in range(1, N):
    a, b, c = map(int, input().split())

    minium[0], minium[1], minium[2] = min(minium[0], minium[1]) + a, min(minium[0], minium[1], minium[2]) + b, min(minium[1], minium[2]) + c
    maxium[0], maxium[1], maxium[2] = max(maxium[0], maxium[1]) + a, max(maxium[0], maxium[1], maxium[2]) + b, max(maxium[1], maxium[2]) + c

print(max(maxium), min(minium))



# N = int(input())
#
# dp = [[[0, 0] for _ in range(3)] for _ in range(N)]
# a, b, c = list(map(int, input().split()))
#
# dp[0][0] = [a, a]
# dp[0][1] = [b, b]
# dp[0][2] = [c, c]
#
# for i in range(1, N):
#     a, b, c = map(int, input().split())
#     prev = i - 1
#
#     dp[i][0][0] = min(dp[prev][0][0], dp[prev][1][0]) + a
#     dp[i][0][1] = max(dp[prev][0][1], dp[prev][1][1]) + a
#
#     dp[i][1][0] = min(dp[prev][0][0], dp[prev][1][0], dp[prev][2][0]) + b
#     dp[i][1][1] = max(dp[prev][0][1], dp[prev][1][1], dp[prev][2][1]) + b
#
#     dp[i][2][0] = min(dp[prev][1][0], dp[prev][2][0]) + c
#     dp[i][2][1] = max(dp[prev][1][1], dp[prev][2][1]) + c
#
# last = dp[N-1]
# mx = max(last[0][1], last[1][1], last[2][1])
# mn = min(last[0][0], last[1][0], last[2][0])
# print(mx, mn)