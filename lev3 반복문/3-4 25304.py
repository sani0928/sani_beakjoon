# total = 총 구매액
# t = 총 구매한 물건 갯수
# 4개 각각의 가격을 더할 변수 설정
# a는 물건가격, b는 물건갯수 a와 b를 곱해 변수에 저장
# 총 t번 반복, 결과는 조건문으로 yes or no

total = int(input()) 
t = int(input())
value = 0

for i in range(t):
    a, b = map(int,input().split())
    value += a * b

print ('Yes' if value == total else 'No')