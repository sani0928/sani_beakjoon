import sys; sys.stdin = open("나머지_합.txt")

N, M = map(int, input().split())
nums = list(map(int, input().split()))
cnt = [0]*M
cnt[0] = 1
ans = 0
r = 0
for num in nums:
    r = (r + num) % M
    ans += cnt[r]
    cnt[r] += 1
print(ans)