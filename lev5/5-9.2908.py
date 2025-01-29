n = list(map(int, input().split()))
reversed_n = [int(str(x)[::-1]) for x in n]
max_val = 0
for i in reversed_n:
    if max_val < i:
        max_val = i
print(max_val)