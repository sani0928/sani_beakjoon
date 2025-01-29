import sys; sys.stdin = open('imachef.txt')

arr = [list(map(int, input().split())) for _ in range(5)]

max_row = 0
max_val = 0

for i in range(5):
    temp = 0
    for j in range(4):
        temp += arr[i][j]
    if max_val < temp:
        max_val = temp
        max_row = i+1

print(max_row, max_val)



''' 14 17 16 16 16'''