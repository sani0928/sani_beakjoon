n = int(input())
num = [int(input()) for _ in range(n)]

num.sort()

print("\n".join(map(str,num)))