def solution(numbers):
    import itertools
    import math
    # str 형태의 숫자를 int 형태로 변환

    num_list = []
    for i in numbers:
        num_list.append(int(i))

    # 만들 수 있는 숫자의 경우의 수를 저장
    tmp = []
    for i in range(1, len(num_list) + 1):
        tmp3 = list(itertools.permutations(num_list, i))
        for j in range(len(tmp3)):
            tmp.append(tmp3[j])

    # 0과 0으로 시작하는 숫자를 제외
    tmp2 = []
    for i in tmp:
        if i[0] != 0:
            tmp2.append(i)

    # 중복 제외
    tmp2 = set(tmp2)

    answer = 0
    for i in tmp2:
        # 1은 소수가 아니므로 제외
        if i[0] == 1 and len(i) == 1:
            continue
        else:
            number = 0
            check = 0
            # n자리 숫자로 변환
            for j in range(len(i)):
                number += (10 ** j) * i[-j - 1]
            # 소수인지 확인(floor함수 이용해서 제곱근까지만 검사)
            for j in range(2, math.floor(math.sqrt(number)) + 1):
                if number % j == 0:
                    check += 1
            if check == 0:
                answer += 1
    return answer