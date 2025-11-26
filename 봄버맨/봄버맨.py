import sys; sys.stdin = open("봄버맨.txt")
dr, dc = (0,0,1,0,-1), (0,1,0,-1,0)
N, M, C = map(int, input().split())
grid = [list(map(str, input().strip())) for _ in range(N)]
memo = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if grid[i][j] == 'O':
            memo[i][j] = 1
t = 1

while True:

    if t == C:
        break

    for r in range(N):
        for c in range(M):
            if memo[r][c] == 0:
                memo[r][c] = 1
            else:
                memo[r][c] += 1
    t += 1
    # for ans in memo:
    #     print(*ans)
    # print('--------')
    if t == C:
        break

    lst = []
    for r in range(N):
        for c in range(M):
            if memo[r][c] != 0:
                if memo[r][c] >= 2:
                    lst.append((r,c))
                else:
                    memo[r][c] += 1

    for r, c in lst:
        for k in range(5):
            nr, nc = r + dr[k], c + dc[k]
            if 0 <= nr < N and 0 <= nc < M:
                memo[nr][nc] = 0
    t += 1
    # for ans in memo:
    #     print(*ans)
    # print('--------')
    if t == C:
        break

for r in range(N):
    ans = []
    for c in range(M):
        if memo[r][c] == 0:
            ans.append('.')
        else:
            ans.append('O')
    print(''.join(ans))
