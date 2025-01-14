# 1654 랜선 자르기

import sys

input = sys.stdin.readline
N, K = map(int, input().split())

rope = []
for _ in range(N):
    length = int(input())
    rope.append(length)

start, end = 1, max(rope)

while (start <= end):
    mid = (start + end) // 2

    num_rope = []
    for i in rope:
        num_rope.append(i // mid)
        
    if (sum(num_rope) < K):
        end = mid - 1
    elif (sum(num_rope) >= K):
        start = mid + 1

print(end)