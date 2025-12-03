import sys; sys.stdin = open("달팽이는_올라가고_싶다.txt")
import math
A, B, V = map(int, input().split())
ans = math.ceil((V - A) / (A - B)) + 1
print(ans)