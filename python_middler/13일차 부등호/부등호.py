# 2529 부등호

N = int(input())
op = list(input().split())

visited = [0] * 10
result = []

def check(a, b, op):
    if (op == "<"):
        if (a > b):
            return False
    
    if (op == ">"):
        if (a < b):
            return False
    
    return True

def dfs(count, num):
    if (count == (N+1)):
        result.append(num)
        return
    
    for i in range(10):
        if (visited[i]):
            continue

        if (count == 0) or (check(num[-1], str(i), op[count-1])):
            visited[i] = 1
            dfs(count+1, num + str(i))
            visited[i] = 0

dfs(0, '')

result.sort()
print(result[-1] + "\n" + result[0])