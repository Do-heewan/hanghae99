# 1707 이분 그래프

import sys

input = sys.stdin.readline
sys.setrecursionlimit(1000000)
K = int(input())

def dfs(num, color):
    visited[num] = True # color라는 임의의 색상 부여 (1 = red)
    colors[num] = color

    for ix in graph[num]:
        if not (visited[ix]):
            a = dfs(ix, -color) # 방문하지 않은 정점인 경우 임의의 색상 blue 부여 (-1 = blue)

            if not a: # 탐색 결과가 false면 false 리턴
                return False

        elif (colors[ix] == colors[num]): # 현재 정점과 다음 정점의 색상이 같은 경우 false 리턴
            return False
    
    return True

for _ in range(K):
    V, E = map(int, input().split())

    graph = [[] for _ in range(V+1)] # 그래프 초기화
    visited = [False] * (V+1) # 방문 표시
    colors = [0] * (V+1) # 방문 표시

    # 그래프 생성
    for _ in range(E):
        a, b = map(int, input().split())
        graph[a] += [b]
        graph[b] += [a]

    # 각 정점을 시작점으로 두고 탐색
    for i in range(1, V+1):
        if not (visited[i]): # 방문하지 않은 정점인 경우만
            result = dfs(i, 1) # (1 = red, -1 = blue)

            if not result: # 탐색 리턴값이 false면 break
                break

    print("YES" if result else "NO")