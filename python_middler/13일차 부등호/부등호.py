# 2529 부등호

import sys
input = sys.stdin.readline

N = int(input())
op = list(input().split())

visited = [False] * 10 # 
result = [] # 결과 저장 리스트

# 부등호 판별
def check(a, b, op):
    if (op == "<"):
        if (a > b):
            return False
    
    if (op == ">"):
        if (a < b):
            return False
    
    return True

# DFS 알고리즘
def dfs(count, num):
    if (count == (N+1)): # 자릿수를 만족하면
        result.append(num) # 리스트에 추가
        return
    
    for i in range(10): # 0 ~ 9까지 탐색
        if not (visited[i]): # 이미 나온 수는 통과 (중복 존재 x)
            if (count == 0) or (check(num[-1], str(i), op[count-1])): # 첫번째 자리 or check()가 참일 경우
                visited[i] = True # 방문 표시
                dfs(count+1, num + str(i)) # 다음 숫자 재귀
                visited[i] = False # 방문 표시 해제

dfs(0, '')

result.sort()
print(result[-1] + "\n" + result[0])