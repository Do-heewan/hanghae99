# 2343 기타 레슨

import sys

input = sys.stdin.readline
N, M = map(int, input().split())
li = list(map(int, input().split()))

start, end = max(li), sum(li) # 시작값 : 가장 큰 용량, 끝값 : 모든 용량의 합

while (start <= end):
    mid = (start + end) // 2

    blueray = 1 # 블루레이 개수
    sum_size = 0 # 하나의 블루레이 안에 담기는 용량의 크기

    for ix in li:
        if ((sum_size + ix) <= mid): # mid보다 작거나 같은 경우(한 블루레이 안에 들어갈 수 있는 최대 용량 만큼 넣은 경우)
            sum_size += ix
        else: # 아닌 경우 -> 블루레이 개수 증가, 두 번째 블루레이에 용량을 더함
            blueray += 1
            sum_size = ix
    
    if (blueray <= M): # 블루레이 개수가 M개를 넘기 직전까지 용량을 줄여야 함
        end = mid - 1
    else:
        start = mid + 1

print(start)