# 2470 두 용액 (두 포인터)

N = int(input())
li = list(map(int, input().split()))
li.sort()

start, end = 0, N-1

answer = abs(li[start] + li[end]) # 가장 작은 합
result = [li[start], li[end]] # 결과 리스트

while (start < end):
    s_val = li[start] # 제일 작은 값
    e_val = li[end] # 제일 큰 값

    sum = s_val + e_val

    if (abs(sum) < answer): # 처음의 합과 이후 연산을 통한 합 비교
        answer = abs(sum) # 더 작은 값이 answer에 들어감
        result = [s_val, e_val] # 그때의 두 용액

        if (answer == 0): # 0이면 최솟값이기에 break
            break
    
    if (sum < 0): # 음수면 작은 값을 증가시킴
        start += 1
    else: # 양수면 큰 값을 감소시킴
        end -= 1

print(result[0], result[1]) # 결과 리스트 출력