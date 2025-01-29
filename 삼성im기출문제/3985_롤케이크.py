import sys;sys.stdin=open('3985_input.txt')
from collections import Counter

L = int(input())
N = int(input())

rollcake = list([0]*(L+1))
lst = [0]
max_val = 0
for i in range(1,N+1):
    P, K = map(int,input().split())

    if max_val < (K-P)+1:
        max_val = K-P
        lst.append(i)
        lst.pop(0)

    for j in range(P,K+1):
        if rollcake[j] == 0:
            rollcake[j] = i
print(*rollcake)
print(*lst)
new_rollcake = []
for k in rollcake:
    if k != 0:
        new_rollcake.append(k)

cnt = Counter(new_rollcake)
max_cnt = max(cnt.values())

print(max_cnt)


a = [1,2,3,4,1,1,2,3,1,1]
print(Counter(a))