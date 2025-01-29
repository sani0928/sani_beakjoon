# case x도 증가
import sys

t = int(input())

for hanroro in range(t):
    a, b = map(int,sys.stdin.readline().split())
    print(f'Case #{hanroro + 1}: {a + b}')


# t = int(input())

# for x in range(t):
#     a, b = map(int,input().split())
#     print(f'Case #{x + 1}: {a + b}')