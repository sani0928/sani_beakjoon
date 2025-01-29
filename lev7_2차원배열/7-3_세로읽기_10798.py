
import sys; sys.stdin = open('10798input.txt')

# arr = [list(map(str, input().split())) for _ in range(n)]
arr = []
# 문자와 정수가 섞여 있을 때 2차원 배열을 어떻게 만들 것인가
n = 5

for _ in range(n):
    row = input()
    converted_row = []
    for i in row:
        if i.isdigit(): # 숫자면 int로 변환 후 저장
            converted_row.append(int(i)) 
        else : # 문자면 그대로 저장
            converted_row.append(i)
    arr.append(converted_row)

result = []
for r in range(n):
    for c in range(n): # 열의 범위는 어떻게 정할 것인가
        result.append(arr[c][r])
        if c < len(arr[r]):
            pass

    print(''.join(result))

'''
AABCDD
afzz
09121
a8EWg6
P5h3kx
'''