import sys; sys.stdin = open("벌집.txt")

# 1, 2~7, 8~19, 20~37, 38~61 ... 1, 1+6, 1+6+12, 1+6+12+18, 1+6+12+18+24

N = int(input())

i = 1
end = 1

while N > end:
    end += 6*i
    i += 1

ans.append(i)