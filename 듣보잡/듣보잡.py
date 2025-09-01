import sys; sys.stdin = open("듣보잡.txt")

N, M = map(int, input().split())

nl = set()
nh = set()
lh = []

for _ in range(N):
    nl.add(input())

for _ in range(M):
    nh.add(input())


if N >= M:
    for i in range(N):
        var = nl.pop()
        if var in nh:
            lh.append(var)

else:
    for i in range(M):
        var = nh.pop()
        if var in nl:
            lh.append(var)

lh.sort()
print(len(lh))
for j in range(len(lh)):
    print(lh[j])