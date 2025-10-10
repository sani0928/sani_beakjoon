import sys; sys.stdin = open("IOIOI.txt")

N = int(input())
M = int(input())
S = tuple(map(str, input().strip()))

ans = 0

for i in range(M):
    if S[i] == 'I':
        idx = i
        p = 0
        result = True
        while p < 2*N+1:

            if idx >= M:
                result = False
                break

            if (p % 2 == 0 and S[idx] != 'I') or (p % 2 != 0 and S[idx] != 'O'):
                result = False
                break

            idx += 1
            p += 1

        if result:
            ans += 1

print(ans)