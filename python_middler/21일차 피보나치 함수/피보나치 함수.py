# 1003 피보나치 함수

zero = [1, 0, 1]
one = [0, 1, 1]

def fibo(num):
    if (num >= 3):
        for i in range(len(zero), num+1):
            zero.append(zero[i-1] + zero[i-2])
            one.append(one[i-1] + one[i-2])

    print(zero[num], one[num])
    
N = int(input())

for _ in range(N):
    fibo(int(input()))