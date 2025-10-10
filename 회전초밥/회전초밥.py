import sys; sys.stdin = open("회전초밥.txt")
from collections import deque

N, d, k, c = map(int,input().split())

sushis = [int(input()) for _ in range(N)]

end = k
ans = 0

q = deque(sushis[:end])

for _ in range(N):

    # 중복 제외 종류
    kinds = len(set(q))

    # 쿠폰번호 초밥이 없다면 제공
    if c not in q:
        tc = kinds + 1
    # 쿠폰번호 초밥이 있다면 제공 x
    else:
        tc = kinds
        ans = tc

    if tc > ans:
        ans = tc

    q.popleft()
    q.append(sushis[end % N])
    end = (end + 1) % N

print(ans)




# N, d, k, c = map(int,input().split())
#
# sushis = []
#
# for _ in range(N):
#     sushis.append(int(input()))
#
# start = 0
# end = start + k
# ans = 0
#
# while start < N:
#
#     # 중복이 있다면 패스
#     if len(set(sushis[start:end])) < k:
#         start = (start % N) + 1
#         end = (end % N) + 1
#
#     else:
#         ans = k
#         print(sushis[start:end])
#         if c not in sushis[start:end]:
#             if start - 1 > 0:
#                 if sushis[start-1] == c:
#                     print(sushis[start-1:end])
#                     ans += 1
#             if end + 1 < N:
#                 if sushis[end+1] == c:
#                     print(sushis[start:end+1])
#                     ans += 1
#
#         start = (start % N) + 1
#         end = (end % N) + 1
#
# print(ans)


# sushis = []
#
#
#
# for _ in range(N):
#     sushis.append(int(input()))
#
# start = 0
# end = start + 2
# cnt = 0
# ans = 0
#
# while start < N:
#
#     cnt += 1
#     print(f'{cnt}턴')
#
#
#     # 중복이 있다면 패스
#     if len(set(sushis[start:end])) < len(sushis[start:end]):
#         start = (start % N) + 1
#         end = (end % N) + 1
#
#     # 중복이 없다면
#     else:
#         e = end
#
#         while sushis[e-1] == c:
#             e = (e % N) + 1
#             # break
#
#         while len(set(sushis[start:e])) == len(sushis[start:e]):
#             e = (e % N) + 1
#
#         print(sushis[start:e])
#
#         # start = (start % N) + 1
#         end = (end % N) + 1
#
# print(ans)