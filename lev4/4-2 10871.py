# 첫째줄에 n과 x
# 둘째줄에 a = 정수 m개
# x보다 작으면 그 수를 출력

n, x = map(int,input().split())
a = list(map(int,input().split()))


# for i in a:
#     if x > i:
#         print(i)


a = [i for i in a if x > i]
print(*a)

# a에 별표는 언패킹 연산자 즉, 리스트의 요소들을 각각의 인자로 전달
# print(a) = [1, 4, 2, 3] (하나의 리스트로 출력) 
# print(*a) = 1 4 2 3 (각각의 인자로 출력)

'''
리스트 컴프리헨션 사용 해보기
[변수이름(i) for i in series if문]
'''