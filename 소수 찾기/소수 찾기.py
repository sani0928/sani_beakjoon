import sys; sys.stdin = open("소수 찾기.txt")

N = int(input())
lst = list(map(int, input().split()))
cnt = 0

for num in lst:
    if num == 1:
        cnt += 1
        continue
    for i in range(2, num):
        if num % i == 0:
            cnt += 1
            break

ans.append (N - cnt)