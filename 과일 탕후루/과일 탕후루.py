import sys; sys.stdin = open("과일 탕후루.txt")
input = sys.stdin.readline
N = int(input())
tanghuru = list(map(int, input().split()))

max_len = 0
start = 0
end = 1

while end != N:
    # print(tanghuru[start:end + 1])
    # set으로 종류 갯수 계산
    cnt = len(set(tanghuru[start:end + 1]))
    if cnt <= 2:
        # print('종류 2개 이하, end 오른쪽으로 1칸 이동')
        # print(f'end와 start = {end}, {start}')
        max_len = max(max_len, end - start + 1)
        end += 1
    else:
        # print('종류 2개 초과, start 오른쪽으로 1칸 이동')
        start += 1
    # print('-------------')

print(max_len)


# 1 1 2 3 1 2 1 1

