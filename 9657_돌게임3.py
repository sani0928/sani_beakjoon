n = int(input())
i = 0
while n != 0:
    if n == 9:
        n -= 4
        i += 1
    elif n == 8:
        n -= 3
        i += 1
    elif n > 5:
        n -= 3
        i += 1
    elif n == 4:
        n -= 4
        i += 1
    elif n <= 3:
        n = 0
        i += 1
    else:
        n -= 1
        i += 1

if i % 2 == 0:
    print('CY')
else:
    print('SK')
