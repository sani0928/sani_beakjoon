import sys; sys.stdin = open("input.txt")
import heapq

N, M = map(int, input().split())
matrix = [list(map(int, input().strip())) for _ in range(N)]
dist_map = [[[float('inf')] * 2 for _ in range(M)] for _ in range(N)]

start_r, start_c = 0, 0
goal_r, goal_c = N - 1, M - 1
dist_map[start_r][start_c][0] = 1

dr, dc = (0, 1, 0, -1), (1, 0, -1, 0)

pq = [(dist_map[start_r][start_c][0], start_r, start_c, 0)]


def going(pq):

    while pq:

        dist, cr, cc, breaking = heapq.heappop(pq)

        if dist > dist_map[cr][cc][breaking]:
            continue

        if cr == goal_r and cc == goal_c:
            return dist

        for k in range(4):
            nr, nc = cr + dr[k], cc + dc[k]
            if 0 <= nr < N and 0 <= nc < M:
                ndist = dist + 1

                # 벽이 있는데 아직 안 부셨다면
                if matrix[nr][nc] == 1 and breaking == 0:
                    if ndist < dist_map[nr][nc][breaking]:
                        dist_map[nr][nc][breaking] = ndist
                        heapq.heappush(pq, (ndist, nr, nc, 1))

                # 갈 수 있는 길이면
                elif matrix[nr][nc] == 0:
                    if ndist < dist_map[nr][nc][breaking]:
                        dist_map[nr][nc][breaking] = ndist
                        heapq.heappush(pq, (ndist, nr, nc, breaking))

    else:
        return -1

ans = going(pq)

ans.append(ans)