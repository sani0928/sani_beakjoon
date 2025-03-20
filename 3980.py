import sys;sys.stdin=open('3980.txt')

T = int(input())
for tc in range(1,T+1):
    matrix = [list(map(int,input().split())) for _ in range(11)]
    visited = [False] * 11
    best_position = 0

    def searchin(lst,row):
        global best_position

        if row == 11:
            best_position = max(best_position, sum(lst))
            return

        for col in range(11):
            if not visited[col] and matrix[row][col] != 0:
                visited[col] = True
                searchin(lst + [matrix[row][col]], row + 1)
                visited[col] = False

    searchin([],0)

    print(best_position)


