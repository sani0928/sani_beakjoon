import sys; sys.stdin = open("연속합.txt")

N = int(input())
arr = list(map(int, input().split()))
cur = best = arr[0]

for i in arr[1:]:
    cur = max(cur + i, i)
    best = max(best, cur)

print(best)