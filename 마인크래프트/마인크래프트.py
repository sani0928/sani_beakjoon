import sys; sys.stdin = open("마인크래프트.txt")

input = sys.stdin.readline

N, M, B = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

min_h = float('inf'); max_h = 0
# 기준 높이 설정
for r in range(N):
    for c in range(M):
        min_h = min(min_h, grid[r][c])
        max_h = max(max_h, grid[r][c])

cnt1 = 0; cnt2 = 0
# 쌓는건 1초, 깎는건 2초
required_cnt = 0
for r in range(N):
    for c in range(M):
        # 쌓을 경우 가정
        if grid[r][c] < max_h:
            required_cnt += (max_h - grid[r][c])
            cnt1 += (max_h - grid[r][c])
        # 깎을 경우 가정
        if grid[r][c] > min_h:
            cnt2 += 2 * (grid[r][c] - min_h)

print(f'min_h: {min_h}, max_h: {max_h}')
print(f'cnt1: {cnt1}, cnt2: {cnt2}')
print(f'required_cnt: {required_cnt}, B: {B}')
# 쌓는게 시간이 더 짧고
if cnt1 < cnt2:
    # 인벤토리 블록이 충분하다면 쌓음
    if B >= required_cnt:
        print('쌓음')
        print(cnt1, max_h)
    # 인벤토리 블록이 부족하다면 할 수 없이 깎음
    else:
        print('깎음')
        print(cnt2, min_h)
# 깎는게 시간이 더 짧다면 깎음
else:
    print('깎음')
    print(cnt2, min_h)