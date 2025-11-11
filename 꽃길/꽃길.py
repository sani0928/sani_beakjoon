import sys; sys.stdin = open("꽃길.txt")
# 5곳 방문처리 및 비용계산, 3개 배치되면 종료
N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
dr, dc = (0,0,1,0,-1), (0,1,0,-1,0)
spot = [(r,c) for r in range(1, N-1) for c in range(1, N-1)]
sold = [[False] * N for _ in range(N)]
ans = 10**9

def check_and_cost(r, c):
    cost = 0
    for k in range(5):
        nr, nc = r + dr[k], c + dc[k]
        if sold[nr][nc]:
            return False, -1
        cost += grid[nr][nc]
    return True, cost

def mark(r, c, flag):

    for k in range(5):
        nr, nc = r + dr[k], c + dc[k]
        sold[nr][nc] = flag
    return

def back(start, total_cost, flowers):
    global ans

    if ans <= total_cost:
        return

    if flowers == 3:
        ans = min(ans, total_cost)
        return

    for i in range(start, len(spot)):
        r, c = spot[i]
        check, cost = check_and_cost(r, c)
        if check:
            mark(r, c, True)
            back(i+1, total_cost + cost, flowers + 1)
            mark(r, c, False)
    return

back(0, 0, 0)
print(ans)