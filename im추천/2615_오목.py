import sys;sys.stdin=open('2615_input.txt')

def check_five(matrix,r,c):

    stone = matrix[r][c]

    for dr,dc in [(1,0),(0,1),(1,1),(-1,1)]: # 4방향: 남쪽,동쪽,남동쪽,북동쪽
        cnt = 1

        nr = r + dr
        nc = c + dc
        while 0<=nr<19 and 0<=nc<19 and matrix[nr][nc] == stone:
            cnt+=1
            nr += dr
            nc += dc
        
        if cnt == 5:
            if  0 <= nr < 19 and 0 <= nc < 19 and matrix[nr][nc] == stone:
                continue

            if dr == 1 and dc == 0:
                if  0 <= r-1 < 19 and matrix[r-1][c] == stone:
                    continue

            if dr == 0 and dc == 1:
                if  0 <= c-1 < 19 and matrix[r][c-1] == stone:
                    continue

            if dr == 1 and dc == 1:
                if  0 <= r-1 < 19 and 0 <= c-1 < 19 and matrix[r-1][c-1] == stone:
                    continue

            if dr == -1 and dc == 1:
                if  0 <= r+1 < 19 and 0 <= c-1 < 19 and matrix[r+1][c-1] == stone:
                    continue

            return stone, r+1, c+1
            
    return 0

matrix = [list(map(int,input().split())) for _ in range(19)]
found = False

for r in range(19):
    if found:
        break
    for c in range(19):
        stone = matrix[r][c]
        if stone == 1 or stone == 2:
            start_r,start_c = r,c
            
            result = check_five(matrix,r,c)
            if result:
                winner_stone, winner_x, winner_y = result
                print(winner_stone)
                print(winner_x, winner_y)
                found = True
                break

if not found:
    print(0)



# 현재 코드 문제점
# 5목 이상 예를 들어 7목이라면 3번째부터 7번째까지 카운팅해 오목으로 판단
# 승부가 결정되지 않았을 때 0 출력