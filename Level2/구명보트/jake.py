from collections import deque

people = [70, 80, 50]
limit = 100
answer = 0
# 우선 크기 순으로 sorting을 해준다.
people = sorted(people)
# 처음에는 index를 받아서 pop(remove하면 너무 오래걸림)을 해줬지만, pop하는 과정도 꽤 오래 걸렸다.
# 그래서 그냥 index끼리 비교하고 숫자만 더하고 빼는 식으로 계산했다.
A = 0
B = len(people)-1
while people:
    #
    if people[A] + people[B] <= limit:
        answer += 1
        B -= 1
        A += 1
    else:
        answer += 1
        B -= 1
    if A > B:
        break
print(answer)

# 오늘의 배운 점
# pop도 시간초과에 큰 영향을 미친다
# index만으로도 가능하면 굳이 pop을 안써도 된다.