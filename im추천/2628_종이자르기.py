import sys;sys.stdin=open('2628_input.txt')

def width_cal(width):

    max_width = 0

    for i in range(1,len(width)):
        temp_w = width[i] - width[i-1]
        if max_width < temp_w:
            max_width = temp_w
    return max_width


def length_cal(length):

    max_length = 0

    for j in range(1,len(length)):
        temp_l = length[j] - length[j-1]
        if max_length < temp_l:
            max_length = temp_l   
    return max_length



w, l = map(int,input().split())
times = int(input())

width = [0, l]
length = [0, w]

for _ in range(times):
    WorL, spot = map(int,input().split())

    if WorL == 0:
        width.append(spot)
    else:
        length.append(spot)

width.sort(reverse=False)
length.sort(reverse=False)

max_width = width_cal(width)
max_length = length_cal(length)
 
print(max_width*max_length)