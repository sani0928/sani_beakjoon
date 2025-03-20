import sys;sys.stdin=open('2210.txt')

matrix = [list(map(int,input().split())) for _ in range(5)]

result = []

def backtrackin(sr,sc,lst):

    if len(lst) == 6:
        i = [i for i in result]
        if lst not in i:
            result.append(lst)
        return

    dr,dc = [0,1,0,-1],[1,0,-1,0]

    for i in range(4):
        nr = sr + dr[i]
        nc = sc + dc[i]
        if 0 <= nr < 5 and 0 <= nc < 5:
            backtrackin(nr,nc,lst + [matrix[nr][nc]])

for r in range(5):
    for c in range(5):
        backtrackin(r, c,[])

print(result)