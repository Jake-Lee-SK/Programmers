def solution(n):
    if n <= 2:
        if n == 1:
            return "1"
        elif n == 2:
            return "2"
    else:
        stack = []
        while 1:
            if n%3 == 0 and n>3:
                stack.append('4')
                n = (n//3)-1
            elif n<=3:
                if n == 3:
                    stack.append('4')
                    break
                else:
                    stack.append(str(n%3))
                    break
            elif n%3 != 0 and n>3:
                stack.append(str(n%3))
                n = n//3
        stack2 = []
        for i in range(len(stack)):
            stack2.append(stack[-1-i])
        return ''.join(stack2)

# 원래 0,1,2 순서로 돌아가는 3진법과 다르게
# 이것은 0이 없으므로 꽤나 특수한 풀이가 필요했다
# 1,2는 그대로 나오지만 4의 경우 3진법 상에서 원래 몫만 있고 나머지가
# 없는 수를 몫을 1을 빼주고 나머지를 4라고 쳐야 하는 굉장한 풀이법