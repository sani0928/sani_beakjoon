import sys; sys.stdin = open("2xn_타일링.txt")

n = int(input())

if n == 1:
    print(1)
    sys.exit(0)
elif n == 2:
    print(2)
    sys.exit(0)

dp = [0] * (n + 1)

dp[1] = 1
dp[2] = 2

for i in range(3, n + 1):
    dp[i] = (dp[i-2] + dp[i-1]) % 10007

print(dp[-1])