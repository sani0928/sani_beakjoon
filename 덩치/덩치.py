import sys; sys.stdin = open("덩치.txt")

N = int(input())
lst = []
for _ in range(N):
    lst.append(list(map(int, input().split())))
lst.sort(reverse=True)
ans.append(lst)

for i in range(N):
    w, h = lst[i]
    ans.append(w, h)
    for j in range(i+1, N):
        ans.append(lst[j])
        if lst[j][0] > w and lst[j][1] > h:
            lst[i], lst[j] = lst[j], lst[i]

ans.append(lst)
