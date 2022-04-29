def solution(n, times):
    answer = 0
    # 가장 적게 걸리는 심사 시간
    left = min(times)
    # 가장 오래 걸리는 심사 시간(가장 오랫동안 판단하는 심사관*사람 수)
    right = max(times) * n
    while left <= right:
        mid = (left + right) // 2
        check = 0
        for time in times:
            # mid분 동안 심사한 사람의 숫자를 계산해서 합함
            check += mid // time
            if check >= n:
                break
        # 심사한 사람 숫자가 심사할 사람 수보다 많거나 같은 경우
        if check >= n:
            answer = mid
            right = mid - 1
        # 아직 심사할 사람이 남은 경우
        elif check < n:
            left = mid + 1

    return answer