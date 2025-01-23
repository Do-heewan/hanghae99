# 2667 단지번호붙이기

from collections import deque
import sys

input = sys.stdin.readline

N = int(input())

# 지도 생성
map = [[] for _ in range(N)]
for i in range(N):
    num = input().strip()
    for ix in num:
        map[i].append(int(ix))

# 방문여부 체크 
visited = [[False] * N for _ in range(N)]

# action(상, 하, 좌, 우)
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

house = 0 # 집의 개수
apart = [] # 집의 개수를 저장하는 리스트(리스트의 길이 = 총 단지수)
for x in range(N):
    for y in range(N):
        # (0, 0) 부터 (N, N)까지 탐색
        if (map[x][y] == 1) and not (visited[x][y]): # (x, y)에 집이 존재하고 방문하지 않은 경우
            visited[x][y] = True # 방문 표시
            house += 1 # 집 개수 카운팅

            Q = deque()
            Q.append([x, y]) # 현재 위치 저장

            while Q:
                cx, cy = Q.popleft()

                # (x,y) -> (x, y+1) / (x, y-1) / (x-1, y) / (x+1, y)
                for i in range(4):
                    nx = cx + dx[i]
                    ny = cy + dy[i]

                    # (x, y)의 상하좌우중 집이 있을 경우 
                    if (0 <= nx < N) and (0 <= ny < N) and (map[nx][ny] == 1) and not (visited[nx][ny]):
                        visited[nx][ny] = True # 방문 체크
                        Q.append((nx, ny)) # 큐에 추가하여 이어서 탐색 진행
                        house += 1 # 집 개수 카운팅

        # 집의 개수가 0인 경우는 존재하지 않음
        if (house != 0):
            apart.append(house) # 리스트에 집 개수 저장
            house = 0 # 0으로 초기화

apart.sort() # 오름차순으로 출력하기 위해 정렬

# 출력
print(len(apart))
for ix in apart:
    print(ix)