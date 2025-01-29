# a는 시간, b는 분, 하루는 1440분

a, b = (map(int,input().split()))

if (a > 0 and b >= 45) or (a == 0 and b >= 45):
    b += - 45
elif (a > 0 and b < 45):
    a -= 1
    b += + 15
elif (a == 0 and b < 45):
    a = 23
    b += + 15

print (a, b)


# b > 45 이면 b - 45
# b < 45 이면 a - 1
# a = 0 이고 b < 45 이면 a = 23

# a = 10
# a = abs(a -15)
# print(a)

# b < 45 일 때 60부터 뒤로.. 