import sys; sys.stdin = open("과제.txt")
N = int(input())
d = [0] * (N+1)
w = [0] * (N+1)
ans = 0

for i in range(1, N+1):
    d[i], w[i] = map(int, input().split())

print(d, w)

day = 0
stop = False
while not stop:
    able = []
    for i in range(1,N+1):
        if d[i] - day > 0:
            able.append(w[i])

    print(able)

    if not able:
        stop = True
        break


    day += 1