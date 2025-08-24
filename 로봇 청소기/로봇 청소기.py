import sys; sys.stdin = open("로봇 청소기.txt")

N, M = map(int, input().split())
r, c, d = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(N)]

# 지나간 길 (청소 칸 확인)
visited = [[False] * M for _ in range(N)]

dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]
ans = 0

while True:
    # 청소할 칸에 있으면 청소하고 카운트 +1
    if not visited[r][c]:
        visited[r][c] = True
        ans += 1
    # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우
    for _ in range(4):
        # 반시계 방향으로 90도 회전
        d = (d + 3) % 4
        nr, nc = r + dr[d], c + dc[d]

        if 0 <= nr < N and 0 <= nc < M:
            # 청소되지 않은 빈 칸으로 이동하고 반복문 탈출
            if not visited[nr][nc] and grid[nr][nc] == 0:
                r, c = nr, nc
                break
    # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
    else:
        back_dir = (d + 2) % 4
        br, bc = r + dr[back_dir], c + dc[back_dir]
        if 0 <= br < N and 0 <= bc < M:
            # 후진할 수 있다면 후진
            if grid[br][bc] == 0:
                r, c = br, bc
            # (grid[br][bc] == 1) 후진 할 수 없다면 작동 중지
            else:
                break

ans.append(ans)