# 1051 숫자 정사각형

import sys

input = sys.stdin.readline

N, M = map(int ,input().split())

# 매트릭스 생성
mat = [[] for _ in range(N)]
for i in range(N):
    word = input()

    for ix in word:
        mat[i].append(ix)

def search(num):
    for i in range(N-num + 1):
        for j in range(M-num + 1):
            if (mat[i][j] == mat[i][j+num-1]) and (mat[i][j] == mat[i+num-1][j]) and (mat[i][j] == mat[i+num-1][j+num-1]): # 꼭짓점 일치 여부 판단
                return True
            
    return False

size = min(N, M) # 두 변중 작은 변 선택

for i in range(size, 0, -1): # 정사각형이 가장 큰 경우부터 탐색
    if (search(i)):
        print(i ** 2)
        
        break