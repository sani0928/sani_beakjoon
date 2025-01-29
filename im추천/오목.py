import sys;sys.stdin=open('2615_input.txt')



def searching_five(r,c,dr,dc,stone):
    cnt = 0
    nr,nc=r,c   

    while 0<=nr<19 and 0<=nc<19 and matrix[nr][nc] == stone:
        cnt += 1
        nr += dr
        nc += dc

    return cnt


def moc(matrix):

    for r in range(19):
        for c in range(19):
            stone = matrix[r][c]
            start_r,start_c = r,c

            if stone == 1 or stone == 2:
                for dr,dc in [(0,1),(1,0),(1,1),(1,-1)]: # 가로, 세로, 대각, 역대각
                    cnt = searching_five(r,c,dr,dc,stone)
                    if cnt == 5:
                        return stone

    return 0

    
matrix = [list(map(int,input().split())) for _ in range(19)]

print(moc(matrix))
    

