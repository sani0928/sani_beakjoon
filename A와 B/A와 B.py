import sys; sys.stdin = open("A와 B.txt")

# 문자열 뒤에 A가 있다면 A를 제거한다.
# 문자열 뒤에 B가 있다면 B를 제거하고 문자열을 뒤집는다.

S = list(map(str, input().strip()))
T = list(map(str, input().strip()))

end = len(S)

while len(T) != end:

    if T[-1] == 'A':
        T.pop()

    else:
        T.pop()
        T.reverse()

if S == T:
    print(1)
else:
    print(0)