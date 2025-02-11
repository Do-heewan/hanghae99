from itertools import permutations
import math

def solution(numbers):
    answer = 0


    # 1. 나올 수 있는 조합 찾기
    all_numbers = []
    number_list = []
    for n in numbers:
        number_list.append(n)

    for i in range(1, len(number_list)+1):
        numbers_len_i = list(permutations(number_list, i))# 자릿수를 변경해가면서 자릿수마다 나올 수 있는 경우의 수를 전체 항목에 더하기
        # numbers_len_i에서 구한 조합의 결과를 사용해서 각 숫자를 모두 하나로 합쳐줘야함
        for j in range(len(numbers_len_i)):
            all_numbers.append(int(''.join(numbers_len_i[j])))

        all_distinct_numbers = set(all_numbers)
        print(all_distinct_numbers)
        all_distinct_numbers = list(all_distinct_numbers)

    #  2. all_distict_numbers에서 소수를 구하기
    for i in range(len(all_distinct_numbers)):
        flag = True
        for j in range(2,int(math.sqrt(all_distinct_numbers[i]))+1):
            if all_distinct_numbers[i] % j == 0:
                flag = False
                break
        if flag == True and all_distinct_numbers[i]!=0  and all_distinct_numbers[i]!=1: 
            #print(all_distinct_numbers[i])            
            answer+=1


    return answer