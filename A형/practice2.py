import sys;sys.stdin=open('practice2.txt')

n, m = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(n)]
times = int(input())

prefix = [[0]*(m+1) for _ in range(n+1)]
for r in range(1,n+1):
    for c in range(1,m+1):
        prefix[r][c] = prefix[r-1][c] + prefix[r][c-1] - prefix[r-1][c-1] + matrix[r-1][c-1]

for _ in range(times):
    i,j,x,y = map(int,input().split())

    result = prefix[x][y] - prefix[i-1][y] - prefix[x][j-1] + prefix[i-1][j-1]

    print(result)