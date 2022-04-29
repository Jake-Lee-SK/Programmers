# stack
import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    s = input()
    answer = len(s)
    for i in range(2, len(s)):
        index = 0
        stack1 = []
        stack2 = []
        final = []
        while index < len(s):
            print(stack1, stack2)
            if len(stack1) != i:
                stack1.append(s[index])
                index += 1
            elif len(stack1) == i:
                stack2.append(s[index])
                index += 1
            elif len(stack1) == i and len(stack2) == i:
                n = ''.join(stack1)
                m = ''.join(stack2)
                if n != m:
                    final.append(n)
                    final.append(m)
                    stack1.clear()
                    stack2.clear()
                    index += 1
                else:
                    final.append('i')
                    final.append(n)
                    stack1.clear()
                    stack2.clear()
                    index += 1
            elif index == len(s)-1:
                final.append(''.join(stack1))
                final.append(''.join(stack2))
                stack1.clear()
                stack2.clear()
                index+=1
        if len(''.join(final)) < answer:
            answer = len(''.join(final))
    print(answer)
