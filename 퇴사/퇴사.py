import sys; sys.stdin = open("퇴사.txt")
N = int(input())

time = [0] * (N + 1)
profit = [0] * (N + 1)

for i in range(1, N + 1):
    time[i], profit[i] = map(int, input().split())

mp = [0] * (N + 2)
for i in range(N, 0, -1):
    skip = mp[i + 1]
    # 퇴사 전에 끝나는 상담이라면 ㄱ
    if i + time[i] <= N + 1:
        take = profit[i] + mp[i + time[i]]
        # 이 일정을 제꼈을 때와 이 일정을 하고 끝난 다음날 최대 이익과 비교해서 더 큰 값 저장
        mp[i] = max(skip, take)
    # 퇴사 전에 끝나는 상담이 아니라면 ㄴ
    else:
        mp[i] = skip

print(mp[1])


