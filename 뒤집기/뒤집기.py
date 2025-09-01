import sys; sys.stdin = open("뒤집기.txt")

S = list(map(int, input().strip()))
s_len = len(S)
cnt_0 = 0; cnt_1 = 0
ans0 = 0; ans1 = 0

for num in S:
    if num == 0:
        cnt_0 += 1
    else:
        cnt_1 += 1

def check():
    global ans0, ans1

    if cnt_0 == s_len or cnt_1 == s_len:
        return 0

    elif cnt_0 == 1 or cnt_1 == 1:
        return 1

    idx0 = 0; idx1 = 0
    # 0만 뒤집
    while idx0 < s_len:
        if S[idx0] == 0:
            ans0 += 1
            while idx0 < s_len:
                if S[idx0] == 1:
                    break
                idx0 += 1
        idx0 += 1
    # 1만 뒤집
    while idx1 < s_len:
        if S[idx1] == 1:
            ans1 += 1
            while idx1 < s_len:
                if S[idx1] == 0:
                    break
                idx1 += 1
        idx1 += 1

    return min(ans0, ans1)

print(check())