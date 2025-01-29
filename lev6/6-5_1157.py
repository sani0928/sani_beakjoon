from collections import Counter

a = input().upper()
b = Counter(a)
c = max(b.values())
# print(a)
# print(b)
# print(c)

num = [i for i, j in b.items() if j == c]

if len(num) == 1:
    print(*num)
else:
    print('?')

# b = list(a.upper())
# # print(b)

# basket = []

# for i in b:
#     basket.append(b.count(i))

# print(max(basket))