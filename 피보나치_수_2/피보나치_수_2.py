import sys; sys.stdin = open("피보나치_수_2.txt")

n = int(input())

lst = [0 for _ in range(n+1)]
lst[1] = 1

for i in range(n-1):
    lst[i+2] = lst[i] + lst[i+1]

print(lst[-1])