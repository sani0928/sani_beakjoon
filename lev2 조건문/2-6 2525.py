
# b + c >= 120 넘으면 a += 2
# b + c >= 180 넘으면 a += 3

# if b --> 60 then a + 1 and b = 0

# b + c >= 60 넘으면 a += 1
# b + c < 60 이면 그냥 b + c

'''
if b + c >= 60 :
    a += (b + c // 60)
    b = 
else :
    b += c
'''
# a는 시, b는 분, c는 소요시간
# if a == 23 :
#     if b + c >= 60:
#         a = 0
#     else :
#         b += c


a, b = map(int,input().split())
c = int(input()) 

if b + c >= 60:
    a += (b + c) // 60
    b = (b + c) % 60
else:
    b += c

a %= 24
print(a, b)

# i = 22 % 24
# print(i)

#연습 : a와 b의 관계
'''
a += ((b + c) // 60)
'''

# 연습: b와 c 관계
'''
b = 48
c = 25
b = (b + c) - 60*((c//60)+1)
print(b)
'''

# i = (48 + 25) // 60
# print(i)

'''
a, b = map(int,input().split())
c = int(input()) 

if b + c >= 60:
    a += ((b + c) // 60)
    b = (b + c) - 60*((c//60)+1)
else:
    b += c
if a >= 24:
    a = 0

print(a, b)
'''