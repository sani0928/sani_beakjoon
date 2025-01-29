# # 출석번호 1~30번
# n=30
# # a = [input() for _ in range(n-2) + list(map(int, a))
# lst = list(map(int, [input() for _ in range(n-2)]))

# # lst를 검사해서 1~30 중 없는 숫자 2개를 발견
# # if _ not in 사용
# # print(lst)


# for x in range(1,n-2):
#     if x not in lst:
#         print(x)

n=30

lst = list(map(int, [input() for _ in range(n-2)]))

for x in range(1,n+1):
    if x not in lst:
        print(x)


# 확실하게 작은 수부터 출력하는 방법
# 리스트 컴플리헨션 사용해 리스트로 변환하고 인덴스 순서대로 출력
# b = [x for x in range(1, n + 1) if x not in lst]
# print(b[0])
# print(b[1])