import sys; sys.stdin = open("마인크래프트.txt")

input = sys.stdin.readline

N, M, B = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

height = [0] * 257
min_h, max_h = float('inf'), 0

for r in range(N):
    for c in range(M):
        height[grid[r][c]] += 1
        min_h = min(min_h, grid[r][c])
        max_h = max(max_h, grid[r][c])

best = float('inf')
ans = -1
# h가 기준 블록 (0~256)
for h in range(min_h, max_h + 1):
    time, inventory = 0, B
    for other_h in range(len(height)):
        # 같은 높이는 제외
        if h == other_h:
            continue
        other_cnt = height[other_h]
        # 쌓음
        if h > other_h:
            time += (h - other_h) * other_cnt
            inventory -= (h - other_h) * other_cnt
        # 깎음
        elif h < other_h:
            time += 2 * (other_h - h) * other_cnt
            inventory += (other_h - h) * other_cnt

    # print(f'기준 블록 높이: {h}, 시간: {time}, 인벤토리: {inventory}')
    if best >= time and inventory >= 0:
        ans = h
        best = time

print(best, ans)