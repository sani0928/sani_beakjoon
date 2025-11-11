import sys; sys.stdin = open("출석체크.txt")
from collections import Counter
N, K, Q, M  = map(int, input().split())
total = [0] * N
sleeping = list(map(int, input().split()))
for s in sleeping:
    total[s-3] = -1
taking_card = list(map(int, input().split()))
for _ in range(M):
    t = total
    print(t)
    S, E = map(int, input().split())
    ran = (E - S) + 1
    for num in taking_card:
        print('시작', num)
        while num < ran + 3:

            print(num - 3)

            if t[num - 3] == -1:
                break

            t[num - 3] = 1

            num += num

            print(t)

    print('답', Counter(t[:ran])[-1] + Counter(t[:ran])[0])