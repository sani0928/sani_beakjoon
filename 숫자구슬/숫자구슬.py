import sys; sys.stdin = open("숫자구슬.txt")

N, M = map(int, input().split())
lst = list(map(int, input().split()))
cnt = [0] * M

print(lst)
