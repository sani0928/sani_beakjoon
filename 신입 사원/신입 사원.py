import sys; sys.stdin = open("신입 사원.txt")

T = int(input())

for tc in range(T):

    N = int(input())
    ans = 0
    interviewee = [[] for _ in range(N + 1)]
    for _ in range(N):
        # 서류점수, 면접점수
        docu, inter = map(int, input().split())
        interviewee[docu] = inter

    max_score = N + 1
    # 서류점수 1등부터 오름차순으로 꼴등 점수(초기값은 N등)와 비교해서 통과 or 탈락 후 가장 낮은 등수 갱신
    for docu_idx in range(1, N + 1):
        if interviewee[docu_idx] < max_score:
            ans += 1
            max_score = interviewee[docu_idx]

    print(ans)
