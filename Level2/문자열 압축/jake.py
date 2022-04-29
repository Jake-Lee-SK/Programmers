# stack

def solution(s):
    # 문자열은 제일 앞부터 정해진 길이만큼 잘라야 합니다.
    
    answer = len(s)
    # 1개부터, 절반까지 잘라서 생각해봄.
    for i in range(1, len(s)//2+1):
        # 새로 만들 단어장
        press = ''
        # 1번째부터 i번째까지 계속되는 문자열
        stack = s[:i]
        count = 1
        # 만약 i+1번부터 2i번까지 같다면
        for j in range(i, len(s), i):
            # 스택을 더해줌
            if s[j:j+i] == stack:
                count += 1
            # 아니라면 지금까지 쌓은 스택을 새로 만들 단어에 저장해나가야 함
            else:
                # count가 2 이상이여야 압축의 의미가 있음
                if count >= 2:
                    press = press + str(count) + stack
                # count가 1이라면 그냥 더해줌
                else:
                    press = press + stack
                # 새로운 반복 문자열 형성
                stack = s[j:j+i]
                count = 1
        # 비교가 끝나고 남은 것도 더해줌
        if count >= 2:
            press = press + str(count) + stack
        else:
            press = press + stack
        # 최소값을 찾는 것이므로 작으면 저장
        if len(press)<answer:
            answer = len(press)
    return answer