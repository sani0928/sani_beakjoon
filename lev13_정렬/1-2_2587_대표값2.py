a = []
for _ in range(5):
    a.append(int(input()))

for i in range(len(a) - 1, 0 , -1):
    for j in range(i):
        if a[j] > a[j + 1]:
            a[j], a[j +1] = a[j + 1], a[j]

total = 0
for k in range(len(a)):
    total += a[k]

print(total//5, a[2])