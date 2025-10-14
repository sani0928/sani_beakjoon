import sys; sys.stdin = open("파도반_수열.txt")

T = int(input())

for _ in range(T):

    N = int(input())
    dp = [1, 1, 1, 1] + ([0] * (N - 3))

    if N <= 3:
        print(1)

    else:
        for i in range(4, N + 1):
            dp[i] = dp[i-3] + dp[i-2]
        print(dp[N])
