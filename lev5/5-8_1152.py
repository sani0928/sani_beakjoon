a = list(input().split(' '))
while '' in a:
    a.remove('')
print(len(a))