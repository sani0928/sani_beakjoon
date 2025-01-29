
'''
26
2+6 = 8
68
6+8 = 14
84
8+4 = 12
42
4+2 = 6
26
'''


n = str(input())
if len(n) == 1:
    n = '0'+n

start_val = n
count= 0

while True:
    sum_val = str(int(n[0]) + int(n[1]))
    n = n[-1] + sum_val[-1]
    count += 1

    if n == start_val:
        break

print(count)


    

