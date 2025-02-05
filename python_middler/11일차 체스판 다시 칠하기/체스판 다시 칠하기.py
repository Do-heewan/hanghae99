# 1018 체스판 다시 칠하기

N, M = map(int, input().split())

mat = [[] for _ in range(N)]
for i in range(N):
    word = input()

    for ix in word:
        mat[i].append(ix)

result = []
for i in range(N-7):
    for j in range(M-7):
        black = 0
        white = 0   
        
        for a in range(i, i+8):
            for b in range(j, j+8):
                if ((a + b) % 2 == 0):
                    if (mat[a][b] != "B"):
                        white += 1
                    if (mat[a][b] != "W"):
                        black += 1
                
                else:
                    if (mat[a][b] != "W"):
                        white += 1
                    if (mat[a][b] != "B"):
                        black += 1
        
        result.append(black)
        result.append(white)

print(min(result))