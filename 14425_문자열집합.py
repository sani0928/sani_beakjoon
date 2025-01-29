import sys; sys.stdin = open('14425_input.txt')


n,m = map(int,input().split())
s = []
count = 0
for _ in range(n):
    s.append(input())

for i in range(m):
    if input() in s:
        count += 1
print(count)