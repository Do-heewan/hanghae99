# 15686 치킨 배달

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

mat = []
for _ in range(N):
    mat.append(list(map(int, input().split())))

homes = []
chickens = []
visited = [[0] * N for _ in range(N)]

ans = []

distance_list = []

for i in range(N):
    for j in range(N):
        if (mat[i][j] == 1):
            homes.append((i, j))
        elif (mat[i][j] == 2):
            chickens.append((i, j))

# 치킨 거리 리턴 함수
def chicken_distance():
    total_distance = 0

    for hx, hy in homes:
        distance = 1e9
        
        for id, (cx, cy) in ans:
            distance = min(distance, abs(hx - cx) + abs(hy - cy))
        
        total_distance += distance

    distance_list.append(total_distance)

# 치킨 집 M개를 고르는 경우의 수
def chicken(count):
    if (count == M):
        chicken_distance()
        return
    
    for id, (cx, cy) in enumerate(chickens):
        if not (visited[cx][cy]):
            if ans and (id < ans[-1][0]):
                continue

            visited[cx][cy] = 1
            ans.append((id, (cx, cy)))

            chicken(count+1)

            visited[cx][cy] = 0
            ans.pop()

chicken(0)
print(min(distance_list))