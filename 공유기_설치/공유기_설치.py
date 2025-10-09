import sys; sys.stdin = open("공유기_설치.txt")

N, C = map(int, input().split())
lst = [int(input()) for _ in range(N)]
lst.sort()
low = lst[0]
high = lst[-1]
