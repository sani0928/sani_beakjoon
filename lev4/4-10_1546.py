# 자기 점수는 최댓값이 m
# m를 기준으로 모든 점수를 '실제점수/(m*100)'
# 첫째 줄은 시험 본 과목 수 = n
# 둘째 줄은 과목 별 점수 = s

n = int(input())
ts = list(map(int,input().split()))
m = max(ts)
fs = 0 # 반복 중에 들어가게 되는 가짜 점수 종합

for x in range(n):
    fs += ts[x] / m * 100
    fs_aver = fs / n

# print('과목수:', n)
# print('최고점수:', m)
print(fs_aver)