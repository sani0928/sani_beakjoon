import sys; sys.stdin = open('1920_input.txt')


n = int(input())
a = set(map(int,input().split()))

m = int(input())
b = list(map(int,input().split()))

# lst = [0] * m

# for i in range(len(b)):
#     for j in range(len(a)):
#         if b[i] == a[j]:
#             lst[i] = 1

for i in b:
    if i in a:
        print(1)
    else:
        print(0)

# for c in lst:     
#     print(c)
