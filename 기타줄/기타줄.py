import sys; sys.stdin = open("기타줄.txt")

N, M = map(int, input().split())

package_price, unit_price = float('inf'), float('inf')
ans = 0

for _ in range(M):
    p_price, u_price = map(int, input().split())
    package_price = min(package_price, p_price)
    unit_price = min(unit_price, u_price)

while N > 0:

    # 줄이 6개 이상이라면
    if N >= 6:
        if package_price < (unit_price * 6):
            ans += package_price
            N -= 6
        else:
            ans += (unit_price * N)
            N = 0
    # 줄이 6개 미만이라면
    else:
        if package_price < (unit_price * N):
            ans += package_price
            N -= 6
        else:
            ans += (unit_price * N)
            N = 0

print(ans)