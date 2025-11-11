import sys; sys.stdin = open("주유소.txt")

N = int(input())
dist = list(map(int, input().split()))
country = list(map(int, input().split()))

min_cost = 10**9
total = 0
i = 0
while i < N-2:
    cost = country[i]
    while cost <= country[i+1] and i < N-2:
        total += cost * dist[i]

        print(i, total)
        i += 1
    cost = country[i]
    total += cost * dist[i]
    i += 1
    print(total)