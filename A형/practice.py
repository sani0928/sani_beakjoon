import sys;sys.stdin=open('practice.txt')

t = int(input())
for tc in range(1,T+1):
    n = int(input())
    arr = list(map(int,input().split()))

    for i in range(1,n):
        for j in range(n-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    print(f'#{tc}', *arr)