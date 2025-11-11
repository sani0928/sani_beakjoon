import sys; sys.stdin = open("나무 재테크.txt")
import heapq
dr,dc = (0,1,1,1,0,-1,-1,-1), (1,1,0,-1,-1,-1,0,1)
tree, dead = [], []
N, M, K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
food = [[5] * N for _ in range(N)]
for _ in range(M):
    x, y, z = map(int, input().split())
    x, y = x-1, y-1
    heapq.heappush(tree, (z,x,y))

def spring():
    temp = []
    for _ in range(len(tree)):
        age, r, c = heapq.heappop(tree)

        if food[r][c] - age >= 0:
            food[r][c] -= age
            age += 1
            temp.append((age, r, c))
        else:
            dead.append((age, r, c))

    while temp:
        heapq.heappush(tree, (temp.pop()))
    return

def summer():
    while dead:
        age, r, c = dead.pop()
        food[r][c] += age // 2
    return

def fall():
    temp = []
    for _ in range(len(tree)):
        age, r, c = heapq.heappop(tree)
        if age % 5 == 0:
            for k in range(8):
                nr, nc = r + dr[k], c + dc[k]
                if 0 <= nr < N and 0 <= nc < N:
                    temp.append((1, nr, nc))
            temp.append((age, r, c))
        else:
            temp.append((age, r, c))

    while temp:
        heapq.heappush(tree, (temp.pop()))
    return

def winter():
    for r in range(N):
        for c in range(N):
            food[r][c] += grid[r][c]
    return

def after_year():
    spring()
    summer()
    fall()
    winter()
    return

year = 0
while year != K:
    after_year()
    year += 1

print(len(tree))