import sys; sys.stdin = open('1236_input.txt')

# 1. 행에 x가 하나도 없으면
# 2. 열에 x가 하나도 없으면
# 3. 행에 x가 있지만 열에 x가 하나도 없다면
# 4. 열에 x가 있지만 행에 x가 하나도 없다면

n,m = map(int, input().split())
matrix = [list(input().strip()) for _ in range(n)]

cnt = 0

for r in range(n):
