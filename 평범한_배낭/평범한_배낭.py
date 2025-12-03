import sys; sys.stdin = open("평범한_배낭.txt")

def back(idx, cur_w, cur_v):
    global max_num

    if K < cur_w:
        return

    for j in range(idx + 1, N):
        if not vis[j]:
            vis[j] = True
            back(j, lst[j][0] + cur_w, lst[j][1] + cur_v)
            vis[j] = False

    max_num = max(max_num, cur_v)
    return

N, K = map(int, sys.stdin.readline().split())
lst = []
for _ in range(N):
    w, v = map(int, sys.stdin.readline().split())
    lst.append((w, v))
lst.sort(reverse=True)
max_num = 0
vis = [False] * N
for i in range(N):
    if lst[i][0] > K:
        continue
    vis[i] = True
    back(i, lst[i][0], lst[i][1])
    vis[i] = False
print(max_num)
