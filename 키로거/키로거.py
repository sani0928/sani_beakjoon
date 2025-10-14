import sys; sys.stdin = open("키로거.txt")

T = int(input())
for _ in range(T):
    put = input()
    left = []
    right = []

    for text in put:

        if text == '<':
            if left:
                right.append(left.pop())
        elif text == '>':
            if right:
                left.append(right.pop())
        elif text == '-':
            if left:
                left.pop()
        else:
            left.append(text)

    print(''.join(left + right[::-1]))
