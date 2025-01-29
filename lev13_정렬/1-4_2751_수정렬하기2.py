

import sys; sys.stdin = open('2751input.txt')
import time

start_time = time.time()

input = sys.stdin.readline

N=int(input())

lst = [int(input()) for _ in range(N)]

result = sorted(lst)

for chunk in result:
    print(chunk)

end_time = time.time()

print (f"{end_time - start_time:.10f} 초")

# = = = = =

# import sys; sys.stdin = open('2751input.txt')
# import time

# start_time = time.time()

# N=int(input())

# lst = [int(input()) for _ in range(N)]

# lst.sort()

# for chunk in lst:
#     print(chunk)

# print(time.time() - start_time)

# = = = = = =
# import sys
# import time
# start_time = time.time()
# N=int(input())
# lst=[]
# for _ in range(N):
#     lst.append(int(input()))
# for i in range(len(lst)-1,0,-1):
#     for j in range(i):
#         if lst[j] > lst[j+1]:
#             lst[j],lst[j+1]=lst[j+1],lst[j]
# for k in range(N):
#     print(lst[k])

# end_time = time.time()

# print (f"{end_time - start_time:.10f} 초")