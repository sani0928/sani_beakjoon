# t로 총 정수 개수 지정
# a는 인풋들을 리스트로 저장
# b는 뽑아내고 싶은 정수
# if문으로 b가 아니면 제거
# 총 b의 개수 출력


t = int(input())
a = list(map(int,input().split()))
b = int(input())
b_count = 0

for i in a:
    if i == b:
        b_count += 1

print(b_count)