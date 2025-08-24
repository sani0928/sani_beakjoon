import sys; sys.stdin = open("팰린드롬수.txt")

while True:
    num = list(map(int, input().strip()))
    if num == [0]:
        break

    length = len(num)

    def radar():
        for i in range(length // 2):
            if num[i] != num[(length - 1) - i]:
                return 'no'

        return 'yes'

    ans.append(radar())
