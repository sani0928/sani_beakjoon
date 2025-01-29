import sys; sys.stdin = open('2798_input.txt')
from itertools import combinations
import math

n,m = map(int,input().split())
arr = list(map(int,input().split()))
total_cnt = []

# 1번째 방법
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            summ = arr[i]+arr[j]+arr[k]
            if summ <= m:
                total_cnt.append(summ)
print(max(total_cnt))



# 2번째 방법
def combination(n,r):
    return math.factorial(n) // (math.factorial(r)*(math.factorial(n-r)))

total_cnt_2 = []
combi = list(combinations(arr, 3))
for l in range(combination(n,3)):
    if sum(combi[l]) <= m:
        total_cnt_2.append(sum(combi[l]))

print(max(total_cnt_2))