a = input()

i = 0
lst = []
while i < len(a):
    j = 0
    temp =''
    while j < 10 and i < len(a):
         temp += a[i]
         j += 1
         i += 1

    lst.append(temp)

for ten in lst:
    print(ten)