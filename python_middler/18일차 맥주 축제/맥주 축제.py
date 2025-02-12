# 17503 맥주 축제

import heapq
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())

# 맥주 종류 순으로 (선호도, 도수)
beers = []
for _ in range(K):
    v, c = map(int, input().split())
    beers.append((v, c))

beers.sort(key = lambda x : x[1]) # 도수 기준으로 정렬

flavor = 0 # 맥주를 마신 후 선호도
heap = [] # 마신 맥주 저장

for beer in beers:
    if (len(heap) < N):
        heapq.heappush(heap, beer) # 맥주를 마시고
        flavor += beer[0] # 선호도 증가

        if (len(heap) == N): # N잔 마셨을 때
            if (flavor >= M): # 선호도가 M 이상이면
                print(beer[1]) # 그 때의 도수가 최솟값
                break
            else:
                flavor -= heapq.heappop(heap)[0] # 가장 처음 마신 맥주

else: # 전체 조건에 맞지 않을 경우
    print(-1)
