t = int(input())

for i in range(t):
    r, s = input().split()
    r = int(r)
    a = [x * r for x in s]
    print(a)
    result=''
    s_length = len([x for x in s])
    for j in range(s_length):
        result += a[j]

    print(result)