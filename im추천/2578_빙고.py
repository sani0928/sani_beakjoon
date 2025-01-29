import sys;sys.stdin=open('2578_input.txt')

def check_three(bingo):

    cnt = 0

    for r in range(n):
        if all(bingo[r][c] == 0 for c in range(n)):
            cnt += 1
    
    for c in range(n):
        if all(bingo[r][c] == 0 for r in range(n)):
            cnt += 1
    
    if all(bingo[i][i] == 0 for i in range(n)):
        cnt += 1
    
    if all(bingo[i][4-i] == 0 for i in range(n)):
        cnt += 1

    return cnt

def bingo_game():

    call = []
    for r in range(n):
        for c in range(n):
            call.append(announce[r][c])
    
    for idx,numbers in enumerate(call):
        for r in range(n):
            for c in range(n):
                if bingo[r][c] == numbers:
                    bingo[r][c] = 0
    
        if idx >= 4:
            if check_three(bingo) >= 3:
                return idx + 1
            
    return 0
    
n = 5
bingo = [list(map(int,input().split())) for _ in range(n)]
announce = [list(map(int,input().split())) for _ in range(n)]

print(bingo_game())
