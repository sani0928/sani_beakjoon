import sys;sys.stdin=open('1592_input.txt')

N,M,L = map(int,input().split())

arr = list([0] * N)
cnt = 0
i = 0
arr[i] += 1
while M not in arr:
    
    if arr[i] % 2 != 0: #홀수면
        arr[(i+L)%N] += 1
        i = (i+L)%N
        cnt+=1

    else: # 짝수면
        arr[(i-L)%N] +=1
        i = (i-L)%N
        cnt+=1

print(cnt)