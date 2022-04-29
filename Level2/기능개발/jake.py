# stack에 앞 날의 배포일수를 확인한 후
# 앞 날보다 뒷 날의 배포일수가 작으면 한꺼번에 배포하는 숫자를 저장
# 뒷날의 배포일수가 크면 stack을 보냄 처리한 후 뒷날의 배포일수를 다시 stack으로 바꿈

def solution(progresses, speeds):
    stack_day = []
    for i in range(len(progresses)):
        if 0 < (100 - progresses[i]) % speeds[i]:
            stack_day.append((100 - progresses[i]) // speeds[i] + 1)
        else:
            stack_day.append((100 - progresses[i]) // speeds[i] )

    stack = stack_day[0]
    days = 1
    spend_days = []
    for i in range(1, len(stack_day)):
        if stack_day[i] <= stack:
            days += 1
            stack_day[i] = 0
        else:
            stack = stack_day[i]
            spend_days.append(days)
            days = 1
    spend_days.append(days)
    return spend_days