import sys; sys.stdin = open("집합.txt")

M = int(input())

s = set()

for _ in range(M):
    cmd = input().split()

    if cmd[0] == 'add':
        if int(cmd[1]) not in s:
            s.add(int(cmd[1]))

    elif cmd[0] == 'remove':
        if int(cmd[1]) in s:
            s.remove(int(cmd[1]))

    elif cmd[0] == 'check':
        print(1 if int(cmd[1]) in s else 0)

    elif cmd[0] == 'toggle':
        if int(cmd[1]) in s:
            s.remove(int(cmd[1]))
        else:
            s.add(int(cmd[1]))

    elif cmd[0] == 'all':
        s = set(i for i in range(1, 21))

    elif cmd[0] == 'empty':
        s = set()