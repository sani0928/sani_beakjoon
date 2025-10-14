import sys; sys.stdin = open("평범한_배낭.txt")

N, K = map(int, input().split())

lst = []

for _ in range(N):
    w, v = map(int, input().split())
    lst.append((v, w))
lst.sort(reverse=True)

max_value = 0
end = 0

while end < N:
    rw = 0
    rv = 0
    for i in range(end, N):
        if rw + lst[i][1] <= K:
            rv += lst[i][0]
            rw += lst[i][1]
        else:
            if max_value < rv:
                max_value = rv
            break

    if max_value < rv:
        max_value = rv

    end += 1

print(max_value)


