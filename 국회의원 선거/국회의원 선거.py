import sys; sys.stdin = open("국회의원 선거.txt")

N = int(input())
if N == 1:
    print(0)
    sys.exit(0)

lst = []
for _ in range(N):
    lst.append(int(input()))

me = lst.pop(0)
ans = 0
max_cnt = max(lst)

while me <= max_cnt:

    idx = -1
    max_cnt = 0
    for i in range(N - 1):
        if lst[i] > max_cnt:
            max_cnt = lst[i]
            idx = i

    lst[idx] -= 1
    max_cnt = max(lst)
    me += 1
    ans += 1

print(ans)



