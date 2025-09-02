import sys; sys.stdin = open("숨바꼭질.txt")
from collections import deque
N, K =  map(int, input().split())
visited = [False] * 200001

q = deque([(N, 0)])
visited[N] = True
ans = 0

def bfs():
    global ans

    while q:
        p, cnt = q.popleft()

        if p == K:
            ans = cnt
            return

        if 0 <= p + 1 < 200001 and not visited[p + 1]:
            print('test1')
            visited[p + 1] = True
            q.append((p + 1, cnt + 1))
        if 0 <= p - 1 < 200001 and not visited[p - 1]:
            print('test2')
            visited[p - 1] = True
            q.append((p - 1, cnt + 1))
        if 0 <= p * 2 < 200001 and not visited[p * 2]:
            print('test3')
            visited[p * 2] = True
            q.append((p * 2, cnt + 1))

    return

bfs()
print(ans)