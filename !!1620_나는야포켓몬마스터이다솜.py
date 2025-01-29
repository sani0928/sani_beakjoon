import sys;sys.stdin=open('1620_input.txt')

n,m = map(int, input().split())
pokemon = list(input() for _ in range (n))

print(pokemon)

for _ in range(m):
    q = input()
    if type(q) == "<class 'int'>":
        print(pokemon[q])
    else: # type(q) == "<class 'str'>"
        print(0)


q = 'bb'
print(type(q))