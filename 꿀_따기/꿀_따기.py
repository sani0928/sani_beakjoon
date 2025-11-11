import sys; sys.stdin = open("꿀_따기.txt")
N = int(input())
arr = list(map(int, input().split()))

pf = [0] * (N+1)
for i in range(1, N+1):
    pf[i] = pf[i-1] + arr[i-1]

best = 0
for j in range(1, N+1):
    honey = j
    for point in range(1, N+1):
        if point != honey:
            for point2 in range(j+1, N+1):
                if point != point2 and point2 != honey:
                    if point > honey and point2 > honey:
                        total = (pf[point-1] - pf[honey-1]) + (pf[point2-1] - pf[honey-1] - arr[point-1])
                        best = max(best, total)
                    elif point > honey:
                        total = (pf[point-1] - pf[honey-1]) + (pf[honey] - pf[point2])
                        best = max(best, total)
                    elif point2 > honey:
                        total = (pf[honey] - pf[point]) + (pf[point2-1] - pf[honey-1])
                        best = max(best, total)
                    else:
                        total = (pf[honey] - pf[point] - arr[point2-1]) + (pf[honey] - pf[point2])
                        best = max(best, total)
print(best)