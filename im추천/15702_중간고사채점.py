# 점수 같으면 가장 낮은 수험번호
import sys;sys.stdin=open('15702_input.txt')

n,m = map(int,input().split())
score = [0] + list(map(int,input().split()))
matrix = [list(map(str,input().split())) for _ in range(m)]

lst = {}
numbers = []
for i in range(m):
    numbers.append(int(matrix[i][0]))

for j in range(m):
    total_score = 0
    for k in range(1, n+1):
        if matrix[j][k] == 'O':
            total_score += score[k]

    lst[int(matrix[j][0])] = total_score

max_score = 0

for l in range(m):
    if max_score < lst[numbers[l]]:
        max_score = lst[numbers[l]]

min_number = 100001
for a in range(m):
    if lst[numbers[a]] == max_score:
        if min_number > numbers[a]:
            min_number = numbers[a]

print('{} {}'.format(min_number,max_score))
    
'''
n,m = map(int,input().split())
score = [0] + list(map(int,input().split()))
matrix = [list(map(str,input().split())) for _ in range(m)]

lst = {}

for j in range(m):
    total_score = 0
    for k in range(1, n+1):
        if matrix[j][k] == 'O':
            total_score += score[k]

    lst[int(matrix[j][0])] = total_score

max_score = 0
min_number = 100001

for l in range(m):
    numbers = int(matrix[l][0])
    if max_score < lst[numbers]:
        max_score = lst[numbers]

        min_number = numbers

    elif lst[numbers] == max_score and numbers < min_number:
        if min_number > numbers:
            min_number = numbers

print('{} {}'.format(min_number,max_score))
'''
