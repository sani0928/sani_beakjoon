'c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z='

# =이 있으면 전 알파벳과 함께 .pop()


alpha = 'ddz=z='
a = [x for x in alpha]
print(a)
counts = 0
for i in a:
    if i == '=':
        a.pop([i]) and a.pop([i-1])
    elif i == '=' and i-1 == 'z' and i-2 == 'd':
        a.pop([i]) and a.pop([i-1] and a.pop([i-2]))        
    if i in '-':
        a.pop([i]) and a.pop([i-1])

print(a)

# '-'와 '='가 있으면 counting x
