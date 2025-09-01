import sys; sys.stdin = open("연구소.txt")
from collections import deque

# 일단 모든 경우의 벽 3개를 세워본다.
# 이후 바이러스를 퍼트린다.
# 모든 경우에서 0의 갯수를 세서 0이 가장 많은 경우 출력
