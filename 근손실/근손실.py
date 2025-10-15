import sys; sys.stdin = open("근손실.txt")
from itertools import permutations
N, K = map(int, input().split())
kits = list(map(int, input().split()))
ans = 0
for permutation in permutations(kits, N):
    weight = 500
    for kit in permutation:
        weight += (kit - K)
        if weight < 500:
            break
    if weight >= 500:
        ans += 1
print(ans)