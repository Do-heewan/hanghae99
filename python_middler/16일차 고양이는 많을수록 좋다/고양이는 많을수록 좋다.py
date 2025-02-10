# 27961 고양이는 많을수록 좋다

import sys
input = sys.stdin.readline

N = int(input())

def cat(N):
    magic_count = 0 # 마법 사용 횟수
    cat_num = 1 # 고양이 수(처음엔 무조건 생성이기에 1마리에서 시작)
    
    while (N > cat_num): # 고양이를 2배 복제하면서, 범위 내에 존재할 경우 stop
        cat_num *= 2
        magic_count += 1

    return magic_count + 1 if N <= cat_num else magic_count + 1 # 복제 횟수 + 처음 생성 횟수

print(cat(N) if N != 0 else 0)