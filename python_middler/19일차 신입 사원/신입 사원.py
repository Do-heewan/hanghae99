# 1946 신입 사원

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())

    people = []
    for _ in range(N):
        a, b = map(int, input().split())
        people.append((a, b))
    
    people.sort(key = lambda x : x[0]) # 서류 성적이 낮은 순 정렬

    pass_num = 1 # 통과한 사람 수
    target = people[0][1] # 서류 성적이 젤 낮은 사람의 면접 등수
    
    # 등수 비교
    for i in range(1, len(people)):
        if (target > people[i][1]): # 등수가 더 크다 -> 순위가 낮다 -> 서류 성적도 낮고 면접 순위도 낮다
            pass_num += 1 # 합격자 한명 추가
            target = people[i][1] # 타겟 변경

    print(pass_num)
