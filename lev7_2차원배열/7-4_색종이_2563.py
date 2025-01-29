import sys; sys.stdin = open('2563input.txt')

t = int(input())

arr = [[0] * 100 for _ in range(100)]

for x in range(1, t+1):
    c1, r1 = map(int, input().split())
    c2,r2 = c1+10, r1+10

    for r in range(r1, r2):
        for c in range(c1, c2):
            arr[r][c] = 1
    
counts = 0
for r in range(100):
    for c in range(100):
        if arr[r][c] == 1:
            counts += 1

print(counts)