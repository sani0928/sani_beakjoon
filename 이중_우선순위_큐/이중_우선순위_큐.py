import sys; sys.stdin = open("이중_우선순위_큐.txt")
import heapq

input = sys.stdin.readline
# D 1 은 최댓값 삭제, D -1은 최솟값 삭제
# Q가 비어있다면 D 무시
T = int(input())

for _ in range(T):
    k = int(input())
    Q = []

    for _ in range(k):

        cmd, num = map(str, input().split())
        num = int(num)

        if cmd == 'I':
            heapq.heappush(Q, num)
        else:
            if Q:
                if num == 1:
                    max_num = max(Q)
                    Q.remove(max_num)
                else:
                    heapq.heappop(Q)

    if Q:
        ans1 = max(Q)
        ans2 = heapq.heappop(Q)
        print(ans1, ans2)
    else:
        print('EMPTY')