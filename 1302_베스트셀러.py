import sys;sys.stdin=open('1302_input.txt')

# n = int(input())
# lst = []
# for _ in range(n):
#     lst.append(input())

# lst2 = set(lst)

# lst3 = []
# max_cnt = 0
# for i in lst2:
#     cnt = 0
#     for j in lst:
#         if i == j:
#             cnt += 1
#             if max_cnt < cnt:
#                 max_cnt = cnt
    
#     lst3.append((list(map(str,(i,cnt)))))

# a_lst = []
# num_lst = []
# for idx,num in lst3:
#     a_lst.append(idx)
#     num_lst.append(int(num))

# result_lst = []
# for k in range(len(a_lst)):
#     if num_lst[k] == max_cnt:
#         result_lst.append(a_lst[k])

# result_lst.sort()

# print(result_lst[0])
        


n = int(input())
lst = []
for _ in range(n):
    lst.append(input())

lst2 = set(lst)

lst3 = []
max_cnt = 0
for i in lst2:
    cnt = 0
    for j in lst:
        if i == j:
            cnt += 1
            if max_cnt < cnt:
                max_cnt = cnt
    lst3.append((list(map(str,(i,cnt)))))

result_lst = []
for alpha,num in lst3:
    if int(num) == max_cnt:
        result_lst.append(alpha)

result_lst.sort()

print(result_lst[0])


# a = ['apple','banana','check']
# lst = []
# for idx,alpha in enumerate(a):
#     lst.append([idx,alpha])

# print(lst)