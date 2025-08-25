import sys; sys.stdin = open("요세푸스 문제 0.txt")

N, K = map(int, input().split())

ans = []
for i in range(N):
    ans.append(((K-1 + K*i) % N) + 1)

print(f'< {", ".join(map(str, ans))} >')