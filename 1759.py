import sys;sys.stdin=open('1759.txt')

L,C = map(int,input().split())
alpha = list(input().split())
alpha.sort()
moeum = ['a', 'e', 'i', 'o', 'u']
result = []

def pw(idx, lst):

    if len(lst) == L:
        moeum_cnt = sum(1 for i in lst if i in moeum)
        jaeum_cnt = L - moeum_cnt

        if moeum_cnt >= 1 and jaeum_cnt >= 2:
            result.append(lst[:])
        return

    for i in range(idx,C):
        lst.append(alpha[i])
        pw(i+1, lst)
        lst.pop()

pw(0, [])


for char in result:
    char.sort()
    print(''.join(char))