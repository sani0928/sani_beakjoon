import sys; sys.stdin = open("숫자 카드 2.txt")
from collections import Counter

input = sys.stdin.readline

N = int(input())
hand = list(map(int, input().split()))
M = int(input())
lst2 = list(map(int, input().split()))

cnt = Counter(hand)
print(cnt[-10])
ans = [cnt[num] for num in lst2]
print(*ans)