# import sys; sys.stdin = open('10989input.txt')

# input = sys.stdin.readline

# N=int(input())

# lst = [int(input()) for _ in range(N)]

# for result in sorted(lst):
#     print(result)

# = = = = = =

import sys; sys.stdin = open('10989input.txt')
# 총 10,000개의 n


input = sys.stdin.readline

n = int(input())

lst = [0] * 10001

for i in range(n):
    num = int(input())
    lst[num] += 1

for j in range(1, 10001):
    if lst[j] != 0:
        for _ in range(lst[j]):
            print(j)


'''
리스트 속 요소를 n개씩 묶는 함수

def group(list, n):
    grouping = [list[i: i + n] for i in range(0,len(list),n)] # 리스트 컴플리헨션 사용
    return grouping

lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
result = group(lst, 5)
print(result)
'''