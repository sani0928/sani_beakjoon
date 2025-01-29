# 0 0이 나오기 전까진 계속 입력하고 출력함

while True:
    a, b = map(int,input().split())
    

    if a == 0 and b == 0:
        break
    print (a + b)



# while a and b:
#     print(a + b)
#     a == 0 and b == 0

# a, b = map(int,input().split())

# for _ in a + b:
#     print(a + b)