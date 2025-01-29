import sys;sys.stdin=open('2961_input.txt')
import math
#신곱쓴합

def combinations(lst,comb_lst,idx,temp_comb):
    if temp_comb:
        comb_lst.append(temp_comb[:])
    
    for i in range(idx,len(lst)):
        temp_comb.append(lst[i])
        combinations(lst,comb_lst,i+1,temp_comb)
        temp_comb.pop()



N = int(input())
s_lst = [] ; b_lst = []

for _ in range(N):
    s, b = map(int,input().split())
    s_lst.append(s) ; b_lst.append(b)

s_comb = []
b_comb = []

combinations(s_lst,s_comb,0,[])
combinations(b_lst,b_comb,0,[])

for c in s_comb:
    print(c)

s_result = []
b_result = []

for j in range(len(s_comb)):
    s_result.append(math.prod(s_comb[j]))
    b_result.append(sum(b_comb[j]))

result = []

for k in range(len(s_result)):
    result.append(abs(s_result[k] - b_result[k]))

print(min(result))