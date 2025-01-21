from collections import deque
import sys

input = sys.stdin.readline

MAX = 10 ** 5 # 입력의 최댓값

N, K = map(int, input().split())
dist = [0] * (MAX + 1) # 방문 표시 및 당시의 거리

def bfs(num):
    Q = deque()
    Q.append(num) # 처음 위치

    while Q:
        c = Q.popleft()

        if (c == K): # 현재 위치가 K와 일치하다면
            return dist[c] # 방문 횟수 리턴

        # 현재 위치에서 다음 위치로 이동하는 경우의 수
        for ix in (c-1, c+1, c*2):
            if (0 <= ix <= MAX) and (dist[ix] == 0): # 다음 위치가 범위에 있고 방문하지 않았더라면
                dist[ix] = dist[c] + 1 # 방문횟수 1 증가
                Q.append(ix) # 큐에 입력해주어 다음 탐색에 이용

print(bfs(N)) # 출력