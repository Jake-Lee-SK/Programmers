def solution(n):
    a = 0
    b = 1
    cnt = 0
    while cnt != n:
        b = a+b
        a = b-a
        cnt += 1
    return a%1234567

# DP 이용