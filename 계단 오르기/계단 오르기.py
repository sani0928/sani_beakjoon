import sys; sys.stdin = open("계단 오르기.txt")

N = int(input())
<<<<<<< HEAD
dp = [0 for _ in range(N+1)]

lst = [0] + list(int(input()) for _ in range(N))

print('계단 lst: ', lst)

dp[1],dp[2] = lst[1], lst[1] + lst[2]

print(f'초기 dp : {dp}')

for i in range(2, N+1):
    dp[i] = max(dp[i-3] + lst[i], dp[i-2] + lst[i])

print(f'최종 dp : {dp}')

print(dp[-1])
=======
lst = list(int(input()) for _ in range(N))
dp = [0] * N

if N == 1:
    print(lst[0])
    sys.exit(0)

elif N == 2:
    print(lst[0] + lst[1])
    sys.exit(0)

dp[0] = lst[0]
dp[1] = lst[0] + lst[1]
dp[2] = max(lst[0] + lst[2], lst[1] + lst[2])

for i in range(3, N):
    dp[i] = max(dp[i-2] + lst[i], dp[i-3] + lst[i-1] + lst[i])

ans = dp[-1]
print(ans)
>>>>>>> 97bad27aaeb32826e95c30e4ef185bad9fe2ef8f
