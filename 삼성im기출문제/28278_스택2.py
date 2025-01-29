import sys;sys.stdin=open('28278_input.txt')

input = sys.stdin.readline

N = int(input())
s = []
for _ in range(N):
    commend = list(map(int,input().split()))
    if commend[0] == 1:
        s.append(commend[1])

    if commend[0] == 2:
        if s:
            print(s.pop())
        else:
            print(-1)

    if commend[0] == 3:
        print(len(s))

    if commend[0] == 4:
        if s:
            print(0)
        else:
            print(1)

    if commend[0] == 5:
        if s:
            print(s[-1])
        else:
            print(-1)