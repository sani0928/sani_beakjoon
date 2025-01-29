'''
같은 눈이 3개가 나오면 10,000원+(같은 눈)*1,000원의 상금을 받게 된다.
같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)*100원의 상금을 받게 된다.
모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)*100원의 상금을 받게 된다.

'''

a, b, c = map(int,input().split())

if a == b == c: # 같은 눈 3개
    a *= 1000
    a += 10000
    print(a)
elif a != b and b != c and a != c: # 다 다른 눈
    if a>=b and a>=c:
        a *= 100
        print(a)
    elif b>=a and b>=c:
        b *= 100
        print(b)
    elif c>=a and c>=b:
        c *= 100
        print(c)
elif a == b or a == c:
    a *= 100
    a += 1000
    print(a)
elif b == a or b == c:
    b *= 100
    b += 1000
    print(b)   
elif c == a or c == b:
    c *= 100
    c += 1000
    print(c)

# 가장 큰 숫자?