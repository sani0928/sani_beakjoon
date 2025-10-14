import sys; sys.stdin = open("과일_탕후루.txt")

N = int(input())
lst = list(map(int, input().split()))

mid = N // 2
left = mid - 1
right = mid + 1
stop_left, stop_right = False, False

while not stop_left and not stop_right:

    if not stop_left:
        print(lst[left:right])
        if len(set(lst[left:right])) > 2:
            stop_left = True
        else:
            left -= 1


    if not stop_right:
        print(lst[left+1:right+1])
        if len(set(lst[left+1:right+1])) > 2:
            stop_right = True
        else:
            right += 1



