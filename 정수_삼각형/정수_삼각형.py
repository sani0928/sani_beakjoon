import sys; sys.stdin = open("정수_삼각형.txt")

N = int(input())
dp = [[0] * i for i in range(1, N+1)]
dp[0][0] = int(input())

for i in range(1, N):
    lst = list(map(int, input().split()))
    for j in range(i + 1):
        num = lst[j]
        if j == 0:
            dp[i][j] = dp[i-1][j] + num
        elif j == i:
            dp[i][j] = dp[i-1][j-1] + num
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + num

print(max(dp[N-1]))