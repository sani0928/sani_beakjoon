import sys; sys.stdin = open("다이어트.txt")

# G = cur**2 - prev**2
# cur > prev

G = int(input())
answer = []

cur = G // 2 + 1
prev = cur - 1

while cur**2 > G:

    if prev == 0:
        cur -= 1
        prev = cur - 1
        continue

    if G == (cur**2 - prev**2):
        print(cur, prev)
        answer.append(cur)
        cur -= 1
        prev = cur - 1
        continue

    prev -= 1

if answer:
    answer.sort()
    for ans in answer:
        print(ans)
else:
    print(-1)