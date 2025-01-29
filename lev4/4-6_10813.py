# 바구니에 공이 한개씩 있음 초기 공 번호는 바구니 번호와 같음
# n은 총 바구니 수, m은 교환 횟수
# i, j는 각각 바꿀 바구니 번호

n, m = map(int,input().split())
lst = list(range(1, n+1))

for x in range(m):
    i, j = map(int,input().split())
    lst[i-1], lst[j-1] = lst[j-1], lst[i-1]
# 리스트의 시작 인덱스가 0이라는 것을 주의
# -1를 안하면 i=1일 때 의도와 달리 1번째 바구니가 아닌 2번째 바구니가 지정됨
print(*lst)


'''
의도한 과정

1 2 3 4 5 #start
2 1 3 4 5
2 1 4 3 5
3 1 4 2 5
3 1 4 2 5
'''

# 두 변수의 교환은 a,b = b,a 이렇게
# a=1, b=2라면 a,b = b,a print(a,b) = 2 1