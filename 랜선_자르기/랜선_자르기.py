import sys; sys.stdin = open("랜선_자르기.txt")

K, N = map(int, input().split())

lans = [int(input()) for _ in range(K)]

low, high = 1, max(lans)
ans = 0

while low <= high:

    mid = (low + high) // 2
    cnt = sum(x // mid for x in lans)

    if cnt >= N:
        ans = mid
        low = mid + 1
    else:
        high = mid - 1

print(ans)