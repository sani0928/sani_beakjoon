import sys; sys.stdin = open("마인크래프트.txt")

input = sys.stdin.readline

N, M, B = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

total_block_h = {}

for r in range(N):
    for c in range(M):
        total_block_h[grid[r][c]] = 0

for r in range(N):
    for c in range(M):
        total_block_h[grid[r][c]] += 1

# print(f'총 블록: {total_block_h}')
ans = 0
min_time = float('inf')
# 총 블록 높이를 하나씩 꺼내서 기준이라 치고 쌓거나 깎거나 하면서 최소 시간 갱신
for k in total_block_h:
    # 총 걸리는 시간, 인벤토리 속 블록 실시간 갱신
    total_time, inventory = 0, B
    for other in total_block_h:
        if other != k:
            # 현재 기준 블록 높이보다 높다면 깎음
            if other > k:
                total_time += 2 * total_block_h[other] * (other - k)
                inventory += total_block_h[other] * (other - k)
            # 현재 기준 블록 높이보다 낮다면 쌓음
            elif other < k:
                total_time += total_block_h[other] * (k - other)
                inventory -= total_block_h[other] * (k - other)
    print(f'현재 기준 블록 높이: {k}, 시간: {total_time}')
    # 인벤토리 확인
    print(f'현재 기준 블록 높이: {k}, 최종 인벤토리: {inventory}')
    if min_time > total_time and inventory >= 0:
       # 답이 여러 개 있다면 그중에서 땅의 높이가 가장 높은 것을 출력하시오.
       if k > ans:
           ans = k
           min_time = total_time

print(min_time, ans)