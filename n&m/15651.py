import sys;sys.stdin=open('15651.txt')

N, M = map(int,input().split())
result = []
def back(idx,lst):

    if len(lst) == M:
        print(*lst)
        return

    for i in range(idx,N+1):
        lst.append(i)
        back(idx+1,lst)
        lst.pop()

back(1,[])


