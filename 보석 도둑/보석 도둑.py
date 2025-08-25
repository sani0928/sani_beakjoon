import sys; sys.stdin = open("보석 도둑.txt")
import heapq

input = sys.stdin.readline

N, K = map(int, input().split())
# 보석 리스트
jewel = [tuple(map(int, input().split())) for _ in range(N)]
C = [int(input()) for _ in range(K)]
ans = 0
# 쥬얼리는 가방 가벼운 순, 가방은 용량 작은 순
jewel.sort()
C.sort()

pq = []
idx = 0
# 가방의 최대 용량 중 가장 비싼 보석을 담는다 (heapq 사용)
for bag in C:
    # 가방에 담을 수 있는 모든 보석을 pq에 추가
    while idx < N and jewel[idx][0] <= bag:
        heapq.heappush(pq, -jewel[idx][1])
        idx += 1
    # 다음 가방은 이전 가방보다 용량이 크므로 pq에 있는 가장 비싼 보석을 담으면 됨
    if pq:
        ans += -heapq.heappop(pq)

print(ans)