import sys; sys.stdin = open("카드2.txt")
from collections import deque

N = int(input())

cards = deque()

for num in range(1, N + 1):
    cards.append(num)

while len(cards) != 1:

    cards.popleft()
    cards.append(cards.popleft())

print(cards.popleft())