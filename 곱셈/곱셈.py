import sys; sys.stdin = open("곱셈.txt")

A, B, C = map(int, input().split())
print(pow(A, B, C))
