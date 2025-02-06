# 2615 오목

import sys
input = sys.stdin.readline

mat = []
for _ in range(19):
    num = list(map(int, input().split()))
    mat.append(num)

# 북동, 동, 남동, 남
dx = [-1, 0, 1, 1]
dy = [1, 1, 1, 0]

for x in range(19):
    for y in range(19):
        if (mat[x][y] != 0):
            start = mat[x][y] # 1 = black / 2 = white

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                count = 1

                while (0 <= nx < 19) and (0 <= ny < 19) and (mat[nx][ny] == start):
                    count += 1

                    if (count == 5): # 5목일때, 6목 체크 or 출력
                        if (0 <= x - dx[i] < 19) and (0 <= y - dy[i] < 19) and (mat[x-dx[i]][y-dy[i]] == start): # 시작점 이전의 돌이 흰 또는 검인지 판단
                            break

                        if (0 <= nx + dx[i] < 19) and (0 <= ny + dy[i] < 19) and (mat[nx+dx[i]][ny+dy[i]] == start): # 끝점 이후의 돌이 흰 또는 검인지 판단
                            break

                        print(start) # 흑 또는 백 승리
                        print(x+1, y+1) # 5개 줄의 시작점
                        sys.exit(0) # 종료코드

                    nx += dx[i]
                    ny += dy[i]

print(0)