import sys; sys.stdin = open("헌내기는_친구가_필요해.txt")
from collections import deque

def catch():

    for r in range(N):
        for c in range(M):
            if campus[r][c] == 'I':
                return r, c
    return

def moving(r, c):
    global ans

    q = deque([(r, c)])
    visited = [[False] * M for _ in range(N)]

    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                if campus[nr][nc] == 'P':
                    ans += 1
                    visited[nr][nc] = True
                    q.append((nr, nc))
                elif campus[nr][nc] == 'O':
                    visited[nr][nc] = True
                    q.append((nr, nc))
    return

dr, dc = (0,1,0,-1), (1,0,-1,0)
N, M = map(int, input().split())
campus = [list(map(str, input().strip())) for _ in range(N)]
ans = 0

sr, sc = catch()
moving(sr, sc)

if ans == 0:
    print('TT')
else:
    print(ans)


