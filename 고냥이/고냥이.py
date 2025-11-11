import sys; sys.stdin = open("고냥이.txt")
from collections import defaultdict

N = int(input())
arr = list(input().strip())
alpha = defaultdict(int)
left = 0
ans = 0
distinct = 0

for right in range(len(arr)):

    if alpha[arr[right]] == 0:
        distinct += 1
    alpha[arr[right]] += 1

    while distinct > N:
        alpha[arr[left]] -= 1
        if alpha[arr[left]] == 0:
            distinct -= 1
        left += 1
    ans = max(ans, right - left + 1)

print(ans)