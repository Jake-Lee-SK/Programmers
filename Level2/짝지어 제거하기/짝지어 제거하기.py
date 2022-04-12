def solution(s):
    if len(s)%2 == 1:
        return 0
    else:
        stack = []
        index = 0
        while index < len(s):
            if not stack:
                stack.append(s[index])
            elif stack[-1] == s[index]:
                stack.pop()
            else:
                stack.append(s[index])
            index += 1
        if not stack:
            return 1
        else:
            return 0

# stack이용하여 시간 줄이기.
# for문 2중으로 돌리면 절대 시간 안에 해결 못함.