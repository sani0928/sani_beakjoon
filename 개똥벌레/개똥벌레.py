import sys; sys.stdin = open("개똥벌레.txt")
input = sys.stdin.readline
N, H = map(int, input().split())
up, down = [0] * (H+1), [0] * (H+1)

for i in range(N):
    stone_h = int(input())
    # 종유석이면(up)
    if i % 2 != 0:
        up[stone_h] += 1
    # 석순이면(down)
    else:
        down[stone_h] += 1

prefix_up, prefix_down = [0] * (H+2), [0] * (H+2)
for j in range(H, 0, -1):
    prefix_up[j] = prefix_up[j+1] + up[j]
    prefix_down[j] = prefix_down[j+1] + down[j]

ans = 10**9
ans2 = 1
for k in range(1,H+1):
    total = (prefix_up[H+1-k]) + (prefix_down[k])
    # print(f'{k}턴에서 {total}번 충돌')
    if ans > total:
        ans = total
        ans2 = 1
    elif ans == total:
        ans2 += 1

print(ans, ans2)


# cnt = [0] * H
#
# for i in range(N):
#     stone_h = int(input())
#     for j in range(H):
#         # 석순이면
#         if i % 2 == 0:
#             if H - (j + 1) < stone_h:
#                 cnt[j] += 1
#         # 종유석이면
#         else:
#             if j < stone_h:
#                 cnt[j] += 1
#
# ans = min(cnt)
# ans2 = 0
# for c in cnt:
#     if c == ans:
#         ans2 += 1
#
# print(ans, ans2)

#
# for j in range(H):
#     cnt = 0
#     for k in range(N):
#         # 석순
#         if k % 2 == 0:
#             if H - (j + 1) < arr[k]:
#                 cnt += 1
#         # 종유석
#         else:
#             if j < arr[k]:
#                 cnt += 1
