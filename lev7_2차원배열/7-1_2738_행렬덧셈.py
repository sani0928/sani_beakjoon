n, m = map(int, input().split())

lst = [list(map(int, input().split())) for _ in range(n*2)]
result = []

for r in range(n):
    r_sum = []
    for c in range(m):
        r_sum.append(lst[r][c] + lst[r + n][c]) # 처음엔 lst[0][0] + lst[4][0] / lst[0][1] + lst[4][1]
    result.append(r_sum)

for i in result:
    print(' '.join(map(str, i)))

    

'''
[1, 1, 1]
[2, 2, 2]
[0, 1, 0]
[3, 3, 3]
[4, 4, 4]
[5, 5, 100]
'''