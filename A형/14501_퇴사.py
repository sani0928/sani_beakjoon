import sys;sys.stdin=open('14501_input.txt')

n = int(input())

schedule = []
for _ in range(n):
    schedule.append(list(map(int,input().split())))

lst = []

j = 0

for i in range(n):
    money = 0
    rest_work = n-i
    while i < n:

        if schedule[i][0] <= rest_work:
            money += schedule[i][1]
            rest_work -= schedule[i][0]

            i += schedule[i][0]
        
        else:
            break
        
    lst.append(money)


print(lst)

# 조건1 : 
    

