import sys; sys.stdin = open("최대_상금(SWEA).txt")

def back(n, cnt):
    global ans, vis

    state = (tuple(n), cnt)
    if state in vis:
        return
    vis.add(state)

    if cnt == K:
        lst_to_num = int(''.join(map(str, n)))
        ans = max(ans, lst_to_num)
        return

    for i in range(len(n)):
        for j in range(i + 1, len(n)):
            n[i], n[j] = n[j], n[i]
            back(n, cnt + 1)
            n[i], n[j] = n[j], n[i]

T = int(input())
for tc in range(1, T + 1):
    ans = 0
    vis = set()
    num, K = map(int, input().split())
    num = list(map(int, str(num).strip()))
    back(num, 0)
    print(f'#{tc} {ans}')
