import sys
sys.stdin = open('input.txt')


def dfs(S, cnt):
    global answer
    if S == len(numbers):
        if cnt == M:
            answer += 1
        return

    check = [0, 0]

    for i in range(2):
        if i == 0:
            check[i] = 1
            dfs(S+1, cnt + numbers[S])
            check[i] = 0
        if i == 1:
            check[i] = 1
            dfs(S+1, cnt - numbers[S])
            check[i] = 0

T = int(input())
for tc in range(1, T+1):
    answer = 0
    M = int(input())
    numbers = list(map(int, input().split()))
    dfs(0, 0)
    print(answer)