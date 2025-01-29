# S = input()
# i = int(input())
# print(S[i-1])

# S = len(input())
# print(S)

# T = int(input())

# for A in range(T):
#     A = input()

#     print(A[0]+A[-1])

# - - -

# if M = a :
#     print('ascending')
# elif M = d :
#     print('descending')
# else print('mixed') :

# - - -

# M = list(map(int, input().split()))

# if M == list(range(1,9)) :
#     print('ascending')
# elif M == list(range(8,0,-1)) :
#     print('descending')
# else :
#     print('mixed')

# a,b,c = map(int,input().split())

# list = [a, b, c]
# list.sort()

# print(list[1])

# i = list(range(int(input())+1))
# i.reverse()
# print(*i)


# for i in list(range(int(input()+1))):
#     if i % 0:
#         print(i)
#     else:
#         pass

# # 가위는 1, 바위는 2, 보는 3

# s = 1
# r = 2
# p = 3

# # A가 이기는 상황 if

# fight = input()

# A,B = map(int, fight.split())

# if (A == s and B == p) or (A == r and B == s) or (A == p and B == r):
#     print('A')
# else:
#     print('B')

# y = int(input())

# if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
#     print('1')
# else:
#     print ('0')


# a = int(input())
# b = int(input())

# if (a>0 and b>0):
#     print(1)
# elif (a<0 and b>0):
#     print(2)
# elif (a<0 and b<0):
#     print(3)
# elif (a>0 and b<0):
#     print(4)

# a는 시간, b는 분, 하루는 1440분

a, b = (map(int,input().split()))

if (a > 0 and b > 45) or (a == 0 and b > 45 ):
    b = b - 45
elif (a > 0 and b < 45):
    a = a - 1
    b = b - 45
elif (a == 0 and b <45 ):
    a = 23
    b = b -45


print (a, b)


# b > 45 이면 b - 45
# b < 45 이면 a - 1
# a = 0 이고 b < 45 이면 a = 23

# a = 10
# a = abs(a -15)
# print(a)