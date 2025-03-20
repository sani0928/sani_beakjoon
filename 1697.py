import sys;sys.stdin=open('1697.txt')
from collections import deque

me, you = map(int,input().split())

visited = [0] * 200001

def bfs(cnt):

    q = deque()
    q.append(me)
    visited[me] = 1

    while q:
        cnt += 1

        position = q.popleft()

        if position == you:
            print(visited[position] - 1)
            return

        if 0<= position*2 < 200001 and visited[position * 2] == 0:
            visited[position * 2] = visited[position] + 1
            q.append(position * 2)

        if 0 <= position+1 < 200001 and visited[position + 1] == 0:
            visited[position + 1] = visited[position] + 1
            q.append(position + 1)

        if 0 <= position-1 < 200001 and visited[position - 1] == 0:
            visited[position - 1] = visited[position] + 1
            q.append(position - 1)

bfs(0)

