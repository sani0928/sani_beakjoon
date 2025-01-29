n, m = map(int,input().split())
lst = list(range(1,n+1))

'''
1 2 3 4 5 초기
2 1 3 4 5
2 1 4 3 5
3 4 1 2 5
3 4 1 2 5
i~j까지의 바구니 번호를 역순으로 바꾼다.
'''

# [i:j]
# lst.reverse()
# lst[i-1:j] = lst[i-1:j][::-1]

for _ in range(m):
    i, j = map(int,input().split())
    lst[i-1:j] = lst[i-1:j][::-1]

print(*lst)