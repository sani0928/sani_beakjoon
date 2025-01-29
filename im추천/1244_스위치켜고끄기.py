import sys;sys.stdin=open('1244_input.txt')

n = int(input())
switch = [0] + list(map(int,input().split()))
times = int(input())
for _ in range(times):
    gender, number = map(int,input().split())
    multiple = number
    if gender == 1: #남자면

        multiple = number

        while number < n+1:

            if switch[number] == 0:
                switch[number] = 1
            else:
                switch[number] = 0

            number += multiple

    else: # 여자면
        if switch[number] == 0:
            switch[number] = 1
        else:
            switch[number] = 0

        a=1
        while 1 <= number-a and number+a < n+1:

            if switch[number-a] == switch[number+a]:

                if switch[number-a] == 0:
                    switch[number-a] = 1
                    switch[number+a] = 1
                else:
                    switch[number-a] = 0
                    switch[number+a] = 0
            else:
                break

            a+=1

switch.pop(0)
for i in range(0,n,20):
    print(*switch[i:i+20])
