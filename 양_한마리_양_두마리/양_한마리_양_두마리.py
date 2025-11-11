import sys; sys.stdin = open("양_한마리_양_두마리.txt")

dr, dc = (0,1,0,-1), (1,0,-1,0)
def counting(sr, sc):
    global vis

    s = [(sr, sc)]
    vis[sr][sc] = True
    while s:

        cr, cc = s.pop()
        for k in range(4):
            nr, nc = cr + dr[k], cc + dc[k]
            if 0 <= nr < H and 0 <= nc < W:
                if grid[nr][nc] == '#' and not vis[nr][nc]:
                    vis[nr][nc] = True
                    s.append((nr, nc))
    return 1

t = int(input())
i = 0
while i < t:

    H, W = map(int, input().split())
    grid = [list(map(str, input().strip())) for _ in range(H)]
    ans = 0
    vis = [[False] * W for _ in range(H)]
    for r in range(H):
        for c in range(W):
            if grid[r][c] == '#' and not vis[r][c]:
                ans += counting(r, c)
    print(ans)
    i += 1