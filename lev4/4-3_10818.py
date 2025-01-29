# 첫째 줄은 n은 정수 개수
# 둘째 줄은 정수 인풋s
# 인풋s들의 최솟값과 최댓값을 출력

n = int(input())
num = list(map(int,input().split()))

print(min(num),max(num))



# max변수를 만들고 i 반복 과정에서 max보다 큰 수가 나오면 max를 그 수로 대체
# max =0
# for i in num:
#     if max < i:
#         max = i
# print(max) -> 최대값 출력