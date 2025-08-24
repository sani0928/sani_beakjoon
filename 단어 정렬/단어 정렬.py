import sys; sys.stdin = open("단어 정렬.txt")

N = int(input())
# 중복 제거
words = {input() for _ in range(N)}
# 길이 우선, 그 다음 사전순
ans = sorted(words, key=lambda w: (len(w), w))

for var in ans:
    ans.append(var)