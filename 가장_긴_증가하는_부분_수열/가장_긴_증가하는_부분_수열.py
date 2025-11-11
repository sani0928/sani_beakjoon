import sys; sys.stdin = open("가장_긴_증가하는_부분_수열.txt")

N = int(input().strip())
nums = list(map(int, input().split()))
# 최소 부분수열 길이는 1
memo = [1]*N
for i in range(N):
    for j in range(i):
        if nums[j] < nums[i]:
            # 그동안 가장 긴 오름차순 갯수에 nums[i] 추가
            memo[i] = max(memo[i], memo[j] + 1)

print(max(memo))


1 2 3
1 2 3
1 2 3

prefix_sum
0 0 0 0
0 1 3 6
0 2 6 12
0 3 9 18

(1,1) (2,2)
답 : 10
18 - 6 - 3 + 1 = 10
2 2 3 3
33 - 3 - 20 + 1
33 - 33 + 1
