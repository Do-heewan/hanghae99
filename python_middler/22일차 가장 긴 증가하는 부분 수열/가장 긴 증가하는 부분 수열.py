# 11053 가장 긴 증가하는 부분 수열

import sys
input = sys.stdin.readline

A = int(input())
seq = list(map(int, input().split()))

dp = [1] * A
for i in range(1, A):
    for j in range(i):
        if (seq[i] > seq[j]):
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))