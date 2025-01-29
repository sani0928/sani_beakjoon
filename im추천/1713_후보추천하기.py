import sys;sys.stdin=open('1713_input.txt')


n = int(input())

frame = []

times = int(input())
scoreboard = list([0] * 101)
sequence = list(map(int,input().split()))

for i in sequence:
    if i in frame: 
        scoreboard[i] += 1
    else:
        if len(frame) < n: # 틀이 꽉차기 전
            frame.append(i)
            scoreboard[i] += 1

        else: # 틀이 꽉
            if i in frame:
                scoreboard[i] += 1

            else: # 새로운 학생이라면
                min_score = 1001

                idx = []

            # 기존 틀에 있는 학생들의 스코어 비교 .. 
            # 가장 낮은 스코어 학생 제거 ..  
            # min_score가 같다면 먼저 들어온 학생 제거

                for k in range(len(frame)): # 기존 틀에 있는 학생들의 스코어 비교 .. 
                    if min_score >= scoreboard[frame[k]]:
                        min_score = scoreboard[frame[k]]
                        idx.append(k)

                frame.pop(idx[0])
                scoreboard[frame[idx[0]]] = 0

                frame.append(i)
    
print(frame)
print(scoreboard)

                        