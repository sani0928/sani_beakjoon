import sys;sys.stdin=open('11659_input.txt')

input = sys.stdin.readline

N,M = map(int,input().split())
arr = list(map(int,input().split()))
prefix = [0] * (N+1)
for i in range(1,N+1):
    prefix[i] = prefix[i-1] + arr[i-1]

for k in range(M):
    i,j = map(int,input().split())
    result = prefix[j] - prefix[i-1]
    print(result)