import sys; sys.stdin = open("분해합.txt")

N = int(input())

def divide_and_sum():
    for i in range(1, N + 1):
        if N == i + sum(map(int, str(i))):
            return i

    return 0

ans.append(divide_and_sum())
