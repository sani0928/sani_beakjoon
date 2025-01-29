import sys; sys.stdin = open('2846_input.txt')
n = int(input())
pi = list(map(int,input().split()))
# print(pi)
start = pi[0]
max_height = 0

for i in range(1,n):
    if pi[i] > pi[i-1]:
        continue
    else:
        height = pi[i-1] - start
        max_height = max(max_height, height) # 이전 오르만 크기와 비교
        start = pi[i]

height = pi[-1] - start
max_height = max(max_height, height)

print(max_height)

# 1 2 1 4 6

# 오르막길 기준은 다음 수가 계속 증가하고 있어야 함
# 4 5 6 7 o, 4 5 5 7 x
