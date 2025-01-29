while True:
    try:
        a, b = map(int,input().split())
        print (a + b)
    except EOFError:  # 입력이 종료되면 루프 종료
        break

#except으로 루프 종료 설정ㄹ