# 1260 DFS와 BFS

from collections import deque
import sys

input = sys.stdin.readline

N, M, V = map(int, input().split()) # 정점, 간선, 시작 노드 입력

graph = [[] for _ in range(N+1)] # 그래프 초기화(생성)
visited_dfs = [False] * (N+1) # DFS 진행 시 방문하는 노드 표시
visited_bfs = [False] * (N+1) # BFS 진행 시 방문하는 노드 표시

# 그래프 생성
for _ in range(M):
    a, b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]

# 작은 수 부터 탐색을 진행하기 위해 정렬
for i in range(len(graph)):
    graph[i].sort()

def dfs(v):
    print(v, end = " ") # 시작 노드 출력
    visited_dfs[v] = True # 방문 표시

    for ix in graph[v]: # 시작 노드의 다음 노드 진행
        if not (visited_dfs[ix]): # 방문하지 않은 노드라면
            dfs(ix) # 재귀 호출

def bfs(v):
    print(v, end = " ") # 시작 노드 출력
    visited_bfs[v] = True # 방문 표시
    Q = deque([v]) # 큐 생성

    while Q: # 큐에 내용이 존재하지 않을 때 까지
        c = Q.popleft() # 큐의 왼쪽부터 pop

        for ix in graph[c]: # 시작 노드의 왼쪽 자식 노드의 자식 노드들
            if not (visited_bfs[ix]): # 방문하지 않은 노드라면
                visited_bfs[ix] = True # 방문 표시
                print(ix, end = " ") # 출력
                Q.append(ix) # 큐에 저장

dfs(V)
print()
bfs(V)