import sys; sys.stdin = open("패션왕 신해빈.txt")
from collections import defaultdict
T = int(input())

for _ in range(T):

    N = int(input())
    cloths = defaultdict(list)
    types = []
    for _ in range(N):
        name, type = map(str, input().split())
        if type not in types:
            types.append(type)
        cloths[type].append(name)
    ans = 1
    if len(types) == 1:
        ans *= len(cloths[types[0]])
        print(ans)
    else:
        ans = 0; ans2 = 1
        for i in range(len(types)):
            ans += len(cloths[types[i]])
        for i in range(len(types)):
            ans2 *= len(cloths[types[i]])
        print(ans + ans2)