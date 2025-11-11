import sys; sys.stdin = open("문자열_교환.txt")

arr = list(input().rstrip())
if arr[0] == arr[len(arr) - 1]:
    l, r = 1, len(arr) - 2
else:
    l, r = 0, len(arr) - 2

cnt = 0
while l < r:

    if arr[l] == arr[r]:
        l += 1
    else:
        if arr[l] == 'a' and arr[r] == 'b':
            print(f'left : {l}, right: {r}')
            cnt += 1
            r -= 1
            l += 1
        else:
            r -= 1
            l += 1

print(cnt)