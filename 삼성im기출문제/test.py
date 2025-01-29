import sys;sys.stdin=open('test.txt')

def BT(idx,temp):

    if len(temp) == M*M:
        result.append(temp[:])
    
    for i in range(idx,M):
        temp.append(matrix[i])
        BT(i+1,temp)
        temp.pop()





T = int(input())

for tc in range(1,T+1):
    
    N, M = map(int,input().split())
    
    matrix = [list(map(int,input().split())) for _ in range(N)]

    result = []

    BT(0,[])

    print(result)
