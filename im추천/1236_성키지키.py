import sys; sys.stdin = open('1236_input.txt')

n,m = map(int, input().split())
arr = [input() for _ in range(n)]
for c in arr:
    print(c)
count = 0

#         else:
#             pass

# for c in range(m):
#     for r in range(n):
#         if arr[r][c] == ['.'] * n:
#             count += 1

# for i in range(n):
#     col_values = [row[i] for row in arr]
#     if col_values == ['.'] * n:
#         count += 1
print(count)