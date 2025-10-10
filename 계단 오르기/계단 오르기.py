import sys; sys.stdin = open("계단 오르기.txt")

N = int(input())
dp = [0 for _ in range(N+1)]

lst = [0] + list(int(input()) for _ in range(N))

print('계단 lst: ', lst)

dp[1],dp[2] = lst[1], lst[1] + lst[2]

print(f'초기 dp : {dp}')

for i in range(2, N+1):
    dp[i] = max(dp[i-3] + lst[i], dp[i-2] + lst[i])

print(f'최종 dp : {dp}')

print(dp[-1])