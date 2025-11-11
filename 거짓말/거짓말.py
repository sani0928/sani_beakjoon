import sys; sys.stdin = open("거짓말.txt")

# unknown = 0, known = 1, 몰랐다가 알게됨 = 2
N, M = map(int, input().split())
people = [0] * (N + 1)
bullshit = 0
know_num, *known_people = map(int, input().split())
for i in known_people:
    people[i] = 1
print(people)
for _ in range(M):
    party_num, *party_people = map(int, input().split())
    for j in party_people:
        # 진실을 알고 있다면
        if people[j] == 1:
            break
        # 진실을 모르고 있다면
        elif people[j] == 0:
            # 거짓말을 들음
            people[j] = 2
        bullshit += 1
print(bullshit)