import sys; sys.stdin = open("2580스도쿠.txt")


def check(r, c, lst):

    # 3x3
    for i in range((r // 3)*3, (r // 3)*3 + 2):
        for j in range((c // 3)*3, (c // 3)*3 + 2):
            if grid[i][j] != 0 and grid[r][c] in lst:
                lst.remove(grid[i][j])

    # 가로
    for i in range(9):
        if grid[r][i] != 0 and grid[r][i] in lst:
            lst.remove(grid[r][i])

    # 세로
    for i in range(9):
        if grid[i][c] != 0 and grid[i][c] in lst:
            lst.remove(grid[i][c])

    if len(lst) == 1:
        grid[r][c] = lst[0]
    return

def end_check():

    cnt = 0
    for x in range(9):
        if not 0 in grid[x]:
            cnt += 1
    if cnt == 9:
        return True

    return False


grid = [list(map(int, input().split())) for _ in range(9)]

while True:

    for r in range(9):
        for c in range(9):
            if grid[r][c] == 0:
                check(r, c, [1, 2, 3, 4, 5, 6, 7, 8, 9])

    # for chunk in grid:
    #     print(*chunk)
    # print('--------------')

    if end_check():
        for chunk in grid:
            print(*chunk)
        break