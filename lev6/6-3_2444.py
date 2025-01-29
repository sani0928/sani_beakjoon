

# 예제 입력값 5면 9줄 출력 중앙출력값이 별9줄
# 1 3 5 7 9 7 5 3 1
# 수열 추리 문제
n = int(input())
n2 = 2 * n - 1

'''
sequence = [2 * i - 1 for i in range(1, n)] + [2 * i - 1 for i in range(n, 0, -1)]

# 공백 함수 더하기
for i in range(n2):
    a = sequence[i] * '*'
    space = ' ' * ((n2 - sequence[i] // 2))
    star = '*' * sequence[i]
    print(space + star)

for i in range(n2):
    a = sequence[i] * '*'
    # space = ' ' * ((n2 - sequence[i] // 2))
    star = '*' * sequence[i]
    print(' ' * ((n2 - sequence[i] // 2)) + star)


# center 메서드 사용
for i in range(n2):
    a = sequence[i] * '*'
    # lst = []
    # lst.append(a)
    print(a.center(n2))
'''

for i in range(1, n2 + 1):
    if i <= n:
        fspace = ' ' * (n - i)
        fstar = '*' * (2 * i - 1) # 1 3 5 7 9
        print(fspace + fstar)
    else:
        bspace = ' ' * (i - n) # 1 2 3 4
        bstar = '*' * (2 * (2 * n - i) - 1) # 7 5 3 1
        print(bspace + bstar)