# 인풋은 한수씩 총 9번 입력
# 최댓값을 찾고 그 값이 몇번째인지 찾아내기

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())
g = int(input())
h = int(input())
i = int(input())

t = a,b,c,d,e,f,g,h,i

# 최댓값 출력
max_value = 0
for hanroro in t:
    if max_value < hanroro:
        max_value = hanroro

print(max_value)

# 몇번째인지..?dfgdijksF?G

print(t.index(max_value) + 1)

# 인풋을 따로 적지 말고 간단하게 입력을 저장하는 방법?


