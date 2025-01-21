# 2776 암기왕

import sys

input = sys.stdin.readline

T = int(input())

def search(num, li, e):
    start, end = 0, e-1
    
    while (start <= end):
        mid = (start + end) // 2
        if (num == li[mid]):
            print(1)
            break
        else:
            if (num > li[mid]):
                start = mid + 1
            else:
                end = mid - 1
        
        if (start == mid) or (end == mid):
            print(0)
            break

for _ in range(T):
    # 정답 리스트
    n = int(input())
    n_list = list(map(int, input().split()))

    # 답안지 리스트
    m = int(input())
    m_list = list(map(int, input().split()))

    n_list.sort()

    for ix in m_list:
        search(ix, n_list, n)