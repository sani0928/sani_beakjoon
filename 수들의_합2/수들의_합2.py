import sys; sys.stdin = open("수들의_합2.txt")

N, M = map(int,input().split())
arr = list(map(int, input().split()))
left, right = 0, 0
ans = 0

while right != N:

    if sum(arr[left:right+1]) < M:
        right += 1
    elif sum(arr[left:right+1]) > M:
        if left == right:
            left += 1
            right += 1
        else:
            left += 1
    else:
        ans += 1
        left += 1
        right += 1

print(ans)