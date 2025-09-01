import sys; sys.stdin = open("올림픽.txt")

N, K = map(int, input().split())
lst = []

for _ in range(N):
    nation, g, s, b = map(int, input().split())
    lst.append((g,s,b,nation))
# 금 -> 은 -> 동 순으로 내림차순
lst.sort(reverse=True)

next = 1
fix = 0

prev_g = 0
prev_s = 0
prev_b = 0

for g,s,b,n in lst:
    # 이전과 점수가 동일하면 출력 시 교정값 +1
    if g == prev_g and s == prev_s and b == prev_b:
        fix += 1
    # 하나라도 다르면 교정값 초기화
    else:
        fix = 0
    # 해당 나라라면 랭크(rank - fix) 출력 후 종료
    if n == K:
        print(next-fix)
        break
    # 이전 금은동 갯수 갱신
    prev_g = g; prev_s = s; prev_b = b
    #
    next += 1
