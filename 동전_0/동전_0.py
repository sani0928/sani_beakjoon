import sys; sys.stdin = open("동전_0.txt")

N, K = map(int,input().split())
coins = list(int(input()) for _ in range(N))
coins.sort(reverse=True)

ans = 0
rest = K

for coin in coins:

    if rest == 0:
        break

    if coin <= rest:
        ans += rest // coin
        cnt = rest // coin
        rest -= (coin * cnt)

print(ans)