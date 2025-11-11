import sys; sys.stdin = open("블로그.txt")

N, X = map(int, input().split())
vis_rec = list(map(int, input().split()))
ans = 0; cnt = 1

for i in range(X):
    ans += vis_rec[i]

cur = ans
for i in range(1, N - X + 1):

    l = i - 1; r = i + X - 1
    cur -= vis_rec[l]; cur += vis_rec[r]

    if cur > ans:
        cnt = 1
        ans = cur
    elif cur == ans:
        cnt += 1

if ans == 0:
    print('SAD')
else:
    print(ans)
    print(cnt)