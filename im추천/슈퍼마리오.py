import sys; sys.stdin = open('supermario.txt')

mushrooms = [int(input()) for _ in range(10)]

def supermario(list):

    # 받은 점수의 합을 최대한 100에 가깝게 만들어야 하기 때문에 반복을 시행하며 계속해서 현재 점수와 직전의 점수를 비교해야 함
    current_point = 0
    before_point = 0
    for i in range(10):

        # 입력된 순서대로 순차적으로 point 적립
        current_point += list[i]

        # 반복 시행동안 100과의 거리를 계산
        # current_point가 100에 가까워질 때까지 반복
        # current_point가 before_point보다 100에서 멀어지면 False -> before_point 반환
        if abs(100 - current_point) < abs(100 - before_point): 
            before_point = current_point

        # 만약 두 점수 모두 100과의 거리가 같다면 ex) 120, 80 그 중 큰 수를 출력한다.
        elif abs(100 - current_point) == abs(100 - before_point):
            return max(current_point, before_point)

    return before_point

print(supermario(mushrooms))



