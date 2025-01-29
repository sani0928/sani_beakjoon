import sys;sys.stdin=open('4344_input.txt')

tc = int(input())
for _ in range(tc):
    lst = list(map(int,input().split()))
    n = lst.pop(0)
    sum = 0
    cnt = 0

    for i in lst:
        sum += i

    average = sum / n

    for j in lst:
        if average < j:
            cnt += 1

    result = ((cnt/n)*100)
    print('{:.3f}%'.format(result))