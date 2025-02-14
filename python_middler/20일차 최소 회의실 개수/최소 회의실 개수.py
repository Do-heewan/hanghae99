# 19598 최소 회의실 개수

import heapq
import sys
input = sys.stdin.readline

N = int(input())

time_list = [list(map(int, input().split())) for _ in range(N)]
time_list.sort(key = lambda x : x[0]) # 먼저 시작하는 순으로 정렬

heap = []
heapq.heappush(heap, time_list[0][1]) # 처음 시작하는 강의가 끝나는 시간 삽입

for i in range(1, N):
    start, end = time_list[i] # 다음 강의의 시작 시간과 끝 시간

    if (heap[0] <= start): # 이전 강의의 끝 시간이 다음 강의의 시작 시간보다 작을 경우
        heapq.heappop(heap) # 힙에서 제거 => 강의실을 비움

    heapq.heappush(heap, end) # 끝나는 시간을 강의실에 추가함으로써 강의실을 늘림

print(len(heap))