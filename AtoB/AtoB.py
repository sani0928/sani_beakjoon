import sys; sys.stdin = open("AtoB.txt")
from collections import deque

A, B = map(int, input().split())

q = deque()
q.append((A, 1))

# 2가지 방식으로 계산한 결과값 저장 (초기값 A 저장)
visited = set()
visited.add(A)

def atob():

    while q:
        # 현재 값과 계산 횟수
        num, cnt = q.popleft()
        # 2가지 방식으로 계산
        for next_num in [num * 2, int(str(num) + "1")]:
            # 계산 후 B가 나오면 계산 횟수 + 1 리턴
            if next_num == B:
                return cnt + 1
            # 아직 B가 안 나오면 방문기록에 저장하고 queue 푸쉬
            elif next_num < B and next_num not in visited:
                visited.add(next_num)
                q.append((next_num, cnt + 1))
    # 2가지 계산 방식은 값이 증가만 하기 때문에 B 초과 값은 B를 만들 수 없으니 -1 리턴
    return -1

ans.append(atob())