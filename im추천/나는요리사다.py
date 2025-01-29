import sys; sys.stdin = open('imachef.txt')

arr = [list(map(int, input().split())) for _ in range(5)]
for c in arr:
    print(*c)

max_score = 0
max_chef_num = 0
for r in range(len(arr)):
    score = 0
    for c in range(len(arr[0])):
        score += arr[r][c]
        if max_score < score:
            max_score = score
            max_chef_num += 1

print(max_chef_num, max_score)


''' 14 17 16 16 16'''