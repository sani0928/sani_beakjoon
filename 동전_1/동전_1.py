import sys; sys.stdin = open("동전_1.txt")

n, k = map(int,input().split())

coins = [int(input()) for _ in range(n)]
coins.sort(reverse=True)
print(coins)
rest = k
ans = 0

for coin in coins:
    if coin <= k and rest - coin >= 0:
        ans += rest // coin
        cnt = rest // coin
        rest -= (coin * cnt)
        print(f'코인: {coin}, 횟수: {cnt}, 남은수: {rest}')

print(ans)

