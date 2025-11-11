import sys; sys.stdin = open("통나무_자르기.txt")

L, K, C = map(int, input().split())
available = list(map(int, input().split()))
available.sort()
print(available)
max_len = 10**9
ans = 0
ans2 = 0
i = 0
while i != C and i != len(available):

    spot = available[i]
    min_len = min(L-spot, spot)
    if max_len > min_len:
        max_len = min_len
        ans = min_len
        ans2 = available[i]

    i += 1

print(ans, ans2)