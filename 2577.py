a = int(input())
b = int(input())
c = int(input())

mp = a * b * c
lst = [0] * 10

for i in range(len(str(mp))):
    for j in range(10):
        # integer은 읽을 수 없으므로 문자로 변경하고 비교
        # ex) mp[1] == 7 xx // str(m)[1] == str(7) oo 
        if str(mp)[i] == str(j): 
            lst[j] += 1

for k in lst:
    print(k)