import sys; sys.stdin = open("니가_싫어_싫어_1.txt")

N = int(input())
lst = []
max_length = 0

for _ in range(N):
    intime, outtime = map(int, input().split())
    max_length = max(max_length, outtime)
    lst.append((intime, outtime))

lst.sort()
# 가장 긴 퇴장시간 = 리스트 길이
rec = [0] * max_length

for in_t, out_t in lst:
    for i in range(in_t, out_t):
        rec[i] += 1
# 모기가 가장 많이 있던 시간대 = ans1
ans1 = max(rec)
ans2 = []

j = 0
while True:
    if rec[j] == ans1:
        # 가장 빠른 시간대
        ans2.append(j)
        while rec[j] == ans1:
            j += 1
        # 연속 구간의 마지막
        ans2.append(j)
        break
    j += 1

print(rec)
print(ans1)
print(*ans2)
