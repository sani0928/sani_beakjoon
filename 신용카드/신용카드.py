import sys; sys.stdin = open("신용카드.txt")

T = int(input())
for tc in range(T):
    credit_num = input()
    digits = [int(d) for d in credit_num]

    for i in range(14, -1, -2):
        ii = digits[i] * 2 - 9 if digits[i] > 5 else digits[i] * 2
        digits[i] = ii

    ans = 0
    for j in digits:
        ans += j

    print('T') if ans % 10 == 0 else print('F')