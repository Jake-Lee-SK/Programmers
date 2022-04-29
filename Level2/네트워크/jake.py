n = 3
computers=[[1, 1, 0], [1, 1, 1], [0, 1, 1]]

graph = [[] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if computers[i][j]==1 and j != i:
            graph[i].append(j)
print(graph)
check = [-1]*n

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
if -1 in check:
    network = check.count(-1) + len(set(check)-1)
    print(network)
else:
    network = len(set(check))
    print(network)