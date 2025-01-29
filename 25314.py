# +4마다 long 추가. 8이면 long*2, 28이면 long*7


a = (int(input()) // 4)

for i in range(1 ,a + 1):
    print(f'{max(i)}번')
    


# b = 20 // 4
# print(b)