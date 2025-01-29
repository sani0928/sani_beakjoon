n = int(input())
i=0
while n != 0:

    if n > 2:
        n -= 3
        i += 1
    else:
        n -= 1
        i+= 1

if i % 2 == 0:
    print('CY')
else:
    print('SK')