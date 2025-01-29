import sys;sys.stdin=open('2178_input.txt')

N,M = map(int,input().split())
matrix = [ list(map(int,input().strip())) for _ in range(N)]

visited = [[0] * M for _ in range(N)]

q = [(0,0)]
visited[0][0] = 1

while q:

    r,c = q.pop(0)

    if r == N-1 and c == M-1:
        print(visited[r][c])

    for dr,dc in [(0,1),(1,0),(0,-1),(-1,0)]:
        nr = r + dr
        nc = c + dc
        if 0<=nr<N and 0<=nc<M and matrix[nr][nc] == 1 and visited[nr][nc] == 0:
            visited[nr][nc] = visited[r][c] + 1
            q.append((nr,nc))

