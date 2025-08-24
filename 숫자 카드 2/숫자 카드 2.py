import sys; sys.stdin = open("숫자 카드 2.txt")
from collections import Counter

input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
M = int(input())
lst2 = list(map(int, input().split()))

cnt = Counter(lst)
ans = [str(cnt[num]) for num in lst2]
print(*ans)