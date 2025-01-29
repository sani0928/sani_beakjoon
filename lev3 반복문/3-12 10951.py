while True:
    try:
        a, b = map(int,input().split())
        print (a + b)
    except EOFError:
        break

#except으로 루프 종료 설정ㄹ