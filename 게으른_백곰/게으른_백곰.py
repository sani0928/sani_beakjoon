import sys; sys.stdin = open("게으른_백곰.txt")
from collections import defaultdict

def total(cur):

    left = cur - K; right = cur + K
    if left < 0:
        left = 0
    if right > max_x:
        right = max_x

    return prefix[right+1] - prefix[left]

rocks = [0] * 1000001
N, K = map(int, input().split())
max_x = 0
for _ in range(N):
    g, x = map(int, input().split())
    rocks[x] = g
    max_x = max(max_x, x)

if K > 1000000:
    print(sum(rocks))
    sys.exit(0)

rocks2 = [0] * (max_x + 1)
for i in range(max_x + 1):
    rocks2[i] = rocks[i]

prefix = [0] * (max_x + 2)
for i in range(1, max_x + 2):
    prefix[i] = prefix[i-1] + rocks2[i-1]

ans = 0
for i in range(1, max_x + 2):
    result = total(i)
    ans = max(ans, result)

print(ans)