import sys;sys.stdin=open('2477_input.txt')
import copy
#동1서2남3북4
#첫번째껀두번째,두번째껀첫번째
# lst = [[] for _ in range(4)]

# n = int(input())

# for _ in range(6): # 육각형이므로 6

#     dir, l = map(int,input().split())

#     if dir == 1:
#         lst[0].append(l)
#     elif dir == 2:
#         lst[1].append(l)
#     elif dir == 3:
#         lst[2].append(l)
#     elif dir == 4:
#         lst[3].append(l)

# lst2 = []
# lst3 = []

# for i in range(4):
#     if len(lst[i]) == 2:
#         lst2.append(lst[i])
#     else:
#         lst3.append(lst[i])

# minus_val = lst2[0][0] * lst2[1][1]

# temp_1 = sum(lst3[0])
# temp_2 = sum(lst3[1])

# complete_quadangle = temp_1 * temp_2

# result = (complete_quadangle - minus_val) * n

# print(result)


n = int(input())
edges = []

for _ in range(6): # 육각형이므로 6
    dir, l = map(int,input().split())
    edges.append((dir, l))

max_length = 0 
max_length_idx = 0
max_width = 0 
max_width_idx = 0

for i in range(6):

    dir, l = edges[i]
    if dir in (1,2): # 동, 서 중 안 끊긴 온전한 변
        if max_length < l:
            max_length = l
            max_length_idx = i
    else:  # 북,남 중 안 끊긴 온전한 변
        if max_width < l:
            max_width = l
            max_width_idx = i

complete_quadangle = max_length * max_width

min_length = edges[(max_length_idx+3)%6][1]
min_width = edges[(max_width_idx+3)%6][1]

min_quadangle = min_length * min_width

result = (complete_quadangle - min_quadangle) * n

print(result)