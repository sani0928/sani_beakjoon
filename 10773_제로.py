import sys; sys.stdin = open('10773_input.txt')


k = int(input())

s = []
for i in range(k):
    n = int(input())
    if n == 0:
        s.pop()
    else:
        s.append(n)
        
total_sum = 0
for j in range(len(s)):
    total_sum += s[j]

print(total_sum)