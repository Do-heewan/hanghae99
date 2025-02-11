# ATM

import sys
input = sys.stdin.readline

N = int(input())
time_list = list(map(int, input().split()))
time_list.sort() # 시간 순으로 정렬

time = 0
# 시간을 순차적으로 더해줌
for i in range(len(time_list)):
    for j in range(i+1):
        time += time_list[j]

print(time)