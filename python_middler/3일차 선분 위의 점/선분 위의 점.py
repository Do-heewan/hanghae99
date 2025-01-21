# 11663 선분 위의 점

import sys

input = sys.stdin.readline
N, M = map(int, input().split())

point = list(map(int, input().split()))
point.sort()

def dot_min(a):  # 선분 중 가장 작은 점 구하기 
    start = 0
    end = N - 1
    while start <= end:
        mid = (start + end) // 2

        if point[mid] < a:
            start = mid + 1
        else:
            end = mid - 1
    return end + 1

def dot_max(b):   # 선분 중 가장 큰 점 구하기
    start = 0
    end = N - 1
    while start <= end:
        mid = (start + end) // 2

        if b < point[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return end

for i in range(M):
    a, b = map(int, input().split())
    print(dot_max(b) - dot_min(a) + 1)