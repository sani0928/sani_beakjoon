import sys; sys.stdin = open("방울_마술(SWEA).txt")

T = int(input())
for tc in range(1, T + 1):
    s, K = input().split()
    cup = list(s)
    K = int(K)
    ans = None
    bell = None
    for i in range(3):
        if cup[i] == 'o':
            bell = i
            break
    if bell == 0:
        if K % 2 != 0:
            ans = 1
        else:
            ans = 0
    elif bell == 1:
        if K % 2 != 0:
            ans = 0
        else:
            ans = 1
    else:
        if K == 0:
            ans = 2
        elif K % 2 != 0:
            ans = 1
        else:
            ans = 0
    print(f'#{tc} {ans}')