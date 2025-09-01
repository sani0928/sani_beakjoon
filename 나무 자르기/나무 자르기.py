import sys; sys.stdin = open("나무 자르기.txt")

input = sys.stdin.readline

N, M = map(int, input().split())
woods = list(map(int, input().split()))
start, end = 0, max(woods)

while start <= end:

    cuting_h = (start + end) // 2
    have = 0

    for wood in woods:
        if wood > cuting_h:
            have += wood - cuting_h
<<<<<<< HEAD
=======
        if have >= M:
            break
>>>>>>> 378261636dea018eb225db12a6a8537e258e2920

    if have >= M:
        start = cuting_h + 1
    else:
        end = cuting_h - 1

print(end)