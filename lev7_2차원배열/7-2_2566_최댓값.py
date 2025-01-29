import sys; sys.stdin = open('2566input.txt')
n = 9
m = 9

arr = [list(map(int, input().split())) for _ in range(n)]
print(arr)
max_val, max_r, max_c = 0, 0, 0

for r in range(n):
    for c in range(m):
        if max_val <= arr[r][c]:
            max_val = arr[r][c]
            max_r = r + 1
            max_c = c + 1

print(max_val)
print(max_r, max_c)


