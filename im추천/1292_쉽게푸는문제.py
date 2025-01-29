import sys; sys.stdin = open('1292_input.txt')
n = 1000
lst = []
i= 0
while len(lst) <= 1000:
    lst += [i]*i
    i += 1
a, b = map(int,input().split())
print(sum(lst[a-1:b]))