import sys; sys.stdin = open("과일 탕후루.txt")
N = int(input())
arr = list(map(int, input().split()))
left = 0
ans = 0
check = [0] * 10
distinct = 0

for right in range(N):


    if check[arr[right]] == 0:
        distinct += 1
    check[arr[right]] += 1

    print(check)

    while distinct > 2:

        check[arr[left]] -= 1
        if check[arr[left]] == 0:
            distinct -= 1
        left += 1
    ans = max(ans, right - left + 1)

print(ans)