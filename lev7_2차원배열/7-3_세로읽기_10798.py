

# # arr = [list(map(str, input().split())) for _ in range(n)]
# arr = []
# # 문자와 정수가 섞여 있을 때 2차원 배열을 어떻게 만들 것인가
# n = 5


# result = []
# for c in range(n):
#     for r in range(n):
#         result.append(arr[r][c])



#     print(''.join(result))


'''
AABCDD
afzz
09121
a8EWg6
P5h3kx
'''

arr = [input() for _ in range(5)]

for c in range(15):
    for r in range(5):
        if c < len(arr[r]):
            print(arr[r][c], end='')