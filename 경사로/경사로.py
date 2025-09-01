import sys; sys.stdin = open("경사로.txt")


def goo(grid):
    global cnt

    have = True
    fail = False
    for c in range(N):
        if not fail:
            p = grid[c]
            if c + 1 < N and grid[c + 1] != p:
                next = grid[c + 1]
                if have and next - p == 1:
                    if c - L + 1 >= 0:
                        for i in range(c - L + 1, c + 1):
                            if grid[i] != p:
                                return
                        have = False
                    else:
                        fail = True
                else:
                    fail = True

        if not fail:
            cnt += 1
            return True

    return False

N, L = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
grid = []
grid2 = []
for num in range(N):
    check = False
    for idx in range(N):
        grid.append(g[num][idx])
        grid2.append(g[num][N - 1 - idx])
    check = goo(grid)
    print(num, check)
    if not check:
        goo(grid2)
    grid = []
    grid2 = []

print(cnt)