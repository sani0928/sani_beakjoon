import sys; sys.stdin = open("2805_나무_자르기.txt")

N, M = map(int, input().split())
arr = list(map(int, input().split()))
start, end = 0, max(arr)
ans = None

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for tree in arr:
        if tree > mid:
            cnt += tree - mid
        if cnt >= M:
            break

    if cnt >= M:
        ans = mid
        start = mid + 1
    else:
        end = mid - 1

print(ans)