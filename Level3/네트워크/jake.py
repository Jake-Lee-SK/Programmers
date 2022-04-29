n = 3
computers=[[1, 1, 0], [1, 1, 1], [0, 1, 1]]

# graph 형태로 변환
graph = [[] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if computers[i][j]==1 and j != i:
            graph[i].append(j)
check = [-1]*n

# BFS 이용해서 경우의 수를 측정
for i in range(n):
    if len(graph[i]) == 0:
        continue
    else:
        stacks = []
        stacks.append(graph[i])
        while stacks:
            checks = stacks.pop(0)
            for stack in checks:
                if check[stack] == -1:
                    check[stack] = i
                    stacks.append(graph[stack])
# 혼자 있는 네트워크의 수 + 연결된 네트워크의 수를 측정
if -1 in check:
    network = check.count(-1) + len(set(check)-1)
else:
    network = len(set(check))

print(network)