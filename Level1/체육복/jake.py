def solution(n, lost, reserve):
    # 순서대로 뽑는 그리디이므로 정렬해야 함
    lost = sorted(lost)
    # 우선 잃어버린 사람을 제외하고 정상적인 사람을 저장
    n = n - len(lost)
    # 잃어버렸지만 여분이 있는 경우 제외
    for i in range(len(lost)):
        if lost[i] in reserve:
            reserve.remove(lost[i])
            lost[i] = -1
    # 앞에서부터 뽑아가는데, 자기보다 앞 번호 사람에게 빌려야 수지타산이 맞음
    for i in range(len(lost)):
        if lost[i] != -1 and lost[i]-1 in reserve and lost[i] not in reserve:
            reserve.remove(lost[i]-1)
            lost[i] = -1
            continue
        if lost[i] != -1 and lost[i]+1 in reserve and lost[i] not in reserve:
            reserve.remove(lost[i]+1)
            lost[i] = -1
            continue
    # 정상적인 사람 + 체육복 빌린 사람(혹은 여벌 있는데 도둑맞은놈)
    for i in range(len(lost)):
        if lost[i] == -1:
            n += 1
    answer = n
    return answer