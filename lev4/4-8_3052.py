n = 10

t = list(map(int, [input() for _ in range(1, n+1)]))

# print(t)

# 나머지가 다른 수를 뽑아내자
# a는 각 입력값을 42로 나눈 나머지 리스트
a = [x % 42 for x in t]

# print(a)

# 뽑아낸 a 리스트에서 서로 다른 나머지가 몇 개 있는지 출력

print(len(set(value_list)))

# set()를 통해 중복 인자 제거
# 중복 제거 후 남은 리스트 요소 갯수를 len으로 구함