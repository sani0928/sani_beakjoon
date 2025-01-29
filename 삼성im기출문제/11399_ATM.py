import sys;sys.stdin=open('11399_input.txt')
import itertools

# N = int(input())

# arr = list(map(int,input().split()))

# lst = list(itertools.permutations(arr))
# lst2 = []

# for i in range(len(lst)):
#     summ = 0
#     for j in range(N):
#         summ += sum(lst[i][0:j+1])
    
#     lst2.append(summ)

# print(min(lst2))

def bt(temp):
    if len(temp) == N:
        lst.append(temp[:])
    
    for i in range(N):
        if not selected[i]:
            temp.append(arr[i])
            selected[i] = True
            bt(temp)
            temp.pop()
            selected[i] = False

N = int(input())

arr = list(map(int,input().split()))

lst = []
selected = [False] * N
bt([])
lst2 = []

for j in range(len(lst)):
    val = 0
    for k in range(N):
        val += sum(lst[j][0:k+1])
    lst2.append(val)

print(lst)
print(min(lst2))