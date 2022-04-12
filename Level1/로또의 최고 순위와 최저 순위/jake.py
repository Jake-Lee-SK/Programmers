def solution(lottos, win_nums):
    answer = []
    max_count = 0
    min_count = 0
    for i in lottos:
        if i in win_nums:
            max_count += 1
            min_count += 1
        elif i == 0:
            max_count += 1
        elif i != 0 and i not in win_nums:
            continue
    former = 0
    sooner = 0

    if min_count == 6:
        sooner = 1
    elif min_count == 5:
        sooner = 2
    elif min_count == 4:
        sooner = 3
    elif min_count == 3:
        sooner = 4
    elif min_count == 2:
        sooner = 5
    else:
        sooner = 6

    if max_count == 6:
        former = 1
    elif max_count == 5:
        former = 2
    elif max_count == 4:
        former = 3
    elif max_count == 3:
        former = 4
    elif max_count == 2:
        former = 5
    else:
        former = 6

    answer.append(former)
    answer.append(sooner)
    return answer

# 쉬운 구현 문제
# but 노가다