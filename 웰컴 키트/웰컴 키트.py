import sys; sys.stdin = open("웰컴 키트.txt")

N = int(input())
lst = list(map(int, input().split()))
T, P = map(int, input().split())

ans1 = 0

for size in lst:
    if size % T == 0:
        ans1 += size // T
    else:
        ans1 += (size // T) + 1

ans2 = [(N // P), (N % P)]

ans.append(ans1)
ans.append(*ans2)