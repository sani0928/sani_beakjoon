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