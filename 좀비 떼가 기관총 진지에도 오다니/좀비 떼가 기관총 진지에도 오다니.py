import sys; sys.stdin = open("좀비 떼가 기관총 진지에도 오다니.txt")
# 좀비는 1m씩 전진
# 기관총은 -10, 지뢰는 즉사(단 좀비가 1m일 때)
# Ml은 기관총 사거리, Mk는 1m 기준 기관총 데미지
def shot():
    global target, turn, C

    while target < last + 1:

        print(f'타켓: {target}, turn: {turn}')
        # 좀비가 진지를 습격
        if zombie[0] > Mk:
            print(f'상황 종료: {zombie}')
            return 'No'

        else:
            # 바로 앞에 있고 지뢰가 있고 좀비 체력이 데미지보다 높다면
            if turn == target and C > 0 and zombie[target] > Mk:
                C -= 1

            for i in range(Ml):
                if i == last:
                    break
                print('test:', i)

                hp = zombie[i] - Mk
                if hp <= 0:
                    zombie[i] = 0
                else:
                    zombie[i] = hp

        for idx in range(1, last):
            if zombie[idx-1] == 0:
                while zombie[idx] == 0:
                    zombie.pop()
                    zombie.append(0)
                    print(zombie)
        for idx2 in range(last):
            if zombie[idx2] != 0:
                target = idx2
                break

        print(f'지뢰 갯수: {C}')
        print(f'실시간 좀비 상황: {zombie}')
        print(f'타켓: {target}')
        print('-------------')

        turn += 1

    return 'Yes'

L = int(input())
Ml, Mk = map(int, input().split())
C = int(input())
zombie = [int(input()) for _ in range(L)]

print(f'초기 좀비: {zombie}')

last = len(zombie)
target = 0
turn = 0

print(shot())


