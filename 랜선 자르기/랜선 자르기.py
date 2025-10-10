import sys; sys.stdin = open("랜선 자르기.txt")

min_length = float('inf')

K, N = map(int, input().split())

lan_cable = []
for _ in range(K):
    lan = int(input())
    lan_cable.append(lan)
    min_length = min(min_length, lan)


def go(start, end, mid):

    while start != end:

        cnt = 0

        for length in lan_cable:
            cnt += length // mid

        if cnt >= N:
            return mid

        elif cnt < N:
            end = mid + 1
            mid = (start + end) // 2

ans = go(0, max(lan_cable), (sum(lan_cable) // N))

while True:

    cnt = 0
    for i in lan_cable:
        cnt += (i // ans)

    if cnt < N:
        ans -= 1
        break

    ans += 1

print(ans)




