# 킹=1 퀸=1 룩=2 비숍=2 나이트=2 폰=8
n = list(map(int,input().split()))
fix = [1, 1, 2, 2, 2, 8]

lst = []

for i in range(6):
    a = fix[i] -n[i]
    lst.append(a)

print(*lst)


# 정해진 피스 개수 존재
# 출력은 '정해진 피스 개수 - 입력값' 반복문으로 출력
# 빈 리스트에 하나씩 추가하고 한번에 출력