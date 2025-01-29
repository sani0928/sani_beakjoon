N=int(input())
lst=[]
for _ in range(N):
    lst.append(int(input()))
for i in range(len(lst)-1,0,-1):
    for j in range(i):
        if lst[j] > lst[j+1]:
            lst[j],lst[j+1]=lst[j+1],lst[j]
for k in range(N):
    print(lst[k])