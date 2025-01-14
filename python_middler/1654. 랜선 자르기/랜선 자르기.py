# 1654 랜선 자르기

import sys

input = sys.stdin.readline
K, N = map(int, input().split())

rope = [] # 랜선의 길이 저장
for _ in range(K):
    length = int(input())
    rope.append(length)

start, end = 1, max(rope)

while (start <= end):
    mid = (start + end) // 2

    num_rope = [] # 자른 후의 랜선의 개수 저장
    for i in rope:
        num_rope.append(i // mid)
        
    if (sum(num_rope) < N): # 랜선의 개수가 필요 랜선의 개수보다 작을 경우
        end = mid - 1 # mid값을 조정하여 더 잘개 자르도록 조정
    elif (sum(num_rope) >= N): # 랜선의 개수가 필요 랜선의 개수보다 클 경우
        start = mid + 1 # mid값을 조정하여 덜 잘개 자르도록 조정

print(end) # start값이 end값보다 커질 때, while문이 종료되고 이때의 end값이 최대 길이가 된다.