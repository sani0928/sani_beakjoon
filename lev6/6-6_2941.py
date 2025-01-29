import sys; sys.stdin = open('2941input.txt')

cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

alpha = input()

counts = 0
i = 0
while i < len(alpha):
    if alpha[i:i+3] in cro:
        counts += 1
        i += 3

    elif alpha[i:i+2] in cro:
        counts += 1
        i += 2

    else:
        counts += 1
        i += 1

print(counts)

# while문은 인덱스(i)의 증가 속도와 증가 조건을 유연하게 설정할 수 있기 때문에
# 경우에 따라 for문보다 더욱 유용하다.