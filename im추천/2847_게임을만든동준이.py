import sys; sys.stdin = open('2847_input.txt')

n = int(input())
score_lst = []
for _ in range(n):
    score = int(input())
    score_lst.append(score)

count = 0
# 1,0
for i in range(n-2,-1,-1): # 내림차순을 반복문 범위를 뒤에서부터 탐색
    while score_lst[i] >= score_lst[i+1]:
        score_lst[i] -= 1
        count += 1

print(count)
