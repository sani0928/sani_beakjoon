import sys; sys.stdin = open("컨베이어 벨트 위의 로봇.txt")
from collections import deque

N, K = map(int, input().split())

container = deque()
container.append(list(map(int, input().split())))
turn = 1
zero = 0
print(container)

up_spot = (N * 2) - 1
down_spot = (N // 2) + 1



for i in range(len(container)):
    container[i] -= 1
    if container[i] > 0:



