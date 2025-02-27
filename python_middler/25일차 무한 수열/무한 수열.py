# 1351 무한 수열

import sys
input = sys.stdin.readline

N, P, Q = map(int, input().split())

dp = {} # dict 선언
dp[0] = 1

def seq(num):
    if (num in dp): # dict 내부에 N이 존재 할 경우 값을 출력
        return dp[num]
    
    else: # 아닐경우, 함수 재귀 호출로 값을 계산
        dp[num] = seq(num // P) + seq(num // Q)
        return dp[num]

print(seq(N))