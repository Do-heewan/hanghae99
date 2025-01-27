# 2573 빙산

from collections import deque
import sys

sys.setrecursionlimit(10**4)
input = sys.stdin.readline

N, M = map(int, input().split())

# 상하좌우 이동
dx = [0 ,0, -1, 1]
dy = [1, -1, 0, 0]

# 매트릭스 생성
matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))

time = 0 # 빙하가 분리되기까지 걸리는 시간 측정

while (True):
    ice = 0
    visited = [[False] * M for _ in range(N)] # 방문 처리
    sea = [[0] * M for _ in range(N)] # 주변 바다 저장 리스트

    # 매트릭스 완전 탐색
    for x in range(N):
        for y in range(M):
            if (matrix[x][y] != 0) and not (visited[x][y]): # 빙산이고 방문하지 않은 경우
                visited[x][y] = True # 방문 표시

                Q = deque()
                Q.append([x, y])

                while Q:
                    cx, cy = Q.popleft()

                    for i in range(4): # 상하좌우 탐색
                        nx = cx + dx[i]
                        ny = cy + dy[i]

                        if (matrix[nx][ny] == 0): # 인접 노드가 0이고 방문하지 않은 경우
                            sea[cx][cy] += 1

                        elif (matrix[nx][ny] != 0) and not (visited[nx][ny]): # 0이 아닌경우 -> 빙산의 일부이기에 Q에 추가
                            visited[nx][ny] = True
                            Q.append([nx, ny])

                # Q가 비어서 while문이 종료가 된다면 빙하가 더 이상 이어져 있지 않음
                ice += 1

    for x in range(N):
        for y in range(M):
            if (visited[x][y]):
                matrix[x][y] -= sea[x][y]

                if (matrix[x][y] < 0):
                    matrix[x][y] = 0

    # 탐색 이후 빙하의 개수가 2개 이상이면 멈춤
    if (ice >= 2):
        break

    if (ice == 0):
        time = 0
        break
    
    # 시간 증가
    time += 1

print(time)