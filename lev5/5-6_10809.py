# 알파벳 a~z까지 총 26
# 단어 S 입력 후 a~z까지 대입하면서 비교
# a~z 중 단어 S에 포함되지 않으면 -1
# 포함된다면 단어s 기준 위치를 출력 (처음 등장하는 위치 기준)

s = input()
alpha = [chr(i) for i in range(97,123)]
empty = []

for i in alpha:
    empty.append(s.find(i))

print(*empty)