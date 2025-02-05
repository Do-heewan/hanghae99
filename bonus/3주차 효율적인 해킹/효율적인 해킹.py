# 1325 효율적인 해킹

from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[b] += [a]

def bfs(num):
    visited = [0] * (N+1)

    Q = deque()
    Q.append(num)

    visited[num] = 1

    while Q:
        c = Q.popleft()

        for ix in graph[c]:
            if (visited[ix] == 0):
                visited[ix] = 1
                Q.append(ix)

    return (sum(visited) - 1)

count = []
for i in range(1, N+1):
    count.append(bfs(i))

for i in range(len(count)):
    if (count[i] == max(count)):
        print(i+1, end = ' ')