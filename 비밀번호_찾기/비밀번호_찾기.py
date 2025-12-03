import sys; sys.stdin = open("비밀번호_찾기.txt")
N, M = map(int, input().split())
saving = {}
for _ in range(N):
    name, pw = map(str, input().split())
    saving[name] = pw
for _ in range(M):
    print(saving[input()])