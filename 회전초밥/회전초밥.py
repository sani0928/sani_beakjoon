import sys; sys.stdin = open("회전초밥.txt")

N, d, k, c = map(int, input().split())
lst = [int(input()) for _ in range(N)]
lst += lst[:k - 1]

check = [0] * (d + 1)
cnt = 0
for i in range(k):
    if check[lst[i]] == 0:
        cnt += 1
    check[lst[i]] += 1

ans = cnt + (1 if check[c] == 0 else 0)

for i in range(1, N):
    l = lst[i-1]
    check[l] -= 1
    if check[l] == 0:
        cnt -= 1

    r = lst[i+k-1]
    if check[r] == 0:
        cnt += 1
    check[r] += 1

    cur = cnt + (1 if check[c] == 0 else 0)
    if cur > ans:
        ans = cur

print(ans)