import sys; sys.stdin = open("차이를 최대로.txt")

N = int(input())

A = list(map(int, input().split()))
A.sort()
minn = A[:(N//2)]
maxx = A[(N//2):N]

# ans = 0
#
# for i in range(N//2):
#     ans += abs(maxx[i] - minn[i])
#     if i+1 < N//2:
#         ans += abs(minn[i] - maxx[i+1])
#
#     print(ans)
#
# print(ans)

B= []

if N % 2 == 0:
    for i in range(N//2):
        B.append(maxx[i])
        B.append(minn[i])

else:
    for i in range(N//2 + 1):
        B.append(maxx[i])
        if i < N//2:
            B.append(minn[i])

ans = 0
for i in range(N-1):
    ans += abs(B[i] - B[i+1])

print(ans)