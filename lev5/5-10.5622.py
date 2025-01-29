n = input() #.split()은 공백을 기준으로 나눔 .split(',')은 ','를 기준으로 나눔.
n2 = [x for x in n]
counts = 0
for i in n2:
    if i in 'ABC':
        counts += 3
    if i in 'DEF':
        counts += 4
    if i in 'GHI':
        counts += 5
    if i in 'JKL':
        counts += 6
    if i in 'MNO':
        counts += 7
    if i in 'PQRS':
        counts += 8
    if i in 'TUV':
        counts += 9
    if i in 'WXYZ':
        counts += 10

print(counts)