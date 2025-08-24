import sys; sys.stdin = open("직각삼각형.txt")

while True:
    N = list(map(int, input().split()))
    if N == [0, 0, 0]:
        break
    N.sort()
    if N[0]**2 + N[1]**2 == N[2]**2:
        ans.append('right')
    else:
        ans.append('wrong')