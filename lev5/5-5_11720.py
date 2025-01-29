n = int(input())

ne = list(map(int,input().strip()))
print(len(ne))
# .strip() : 앞뒤 공백을 생략
# .strip('a') : 특정 문자 제거 


if len(ne) != n:
    exit()
# n개 숫자를 입력한게 아니라면 exit

print(sum(ne))
