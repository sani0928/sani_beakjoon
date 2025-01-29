N=int(input())
lst=[]
for _ in range(N):
    lst.append(int(input()))

sorted_lst = sorted(lst)

for i in range(len(sorted_lst)):
    print(sorted_lst[i])