import heapq
n = 15
costs = [[0,1,5],[1,2,3],[2,3,3],[3,1,2],[3,0,4],[2,4,6],[4,0,7]]

# MST 알고리즘(크루스칼) 응용
answer = 0
INF = int((((n - 1) * n) / 2) + 1)
graph = [[] for _ in range(n)]
visited = [False] *n
for i in range(len(costs)):
    node = costs[i][0]
    graph[node].append((costs[i][1], costs[i][2]))

now_node = 0

for i in range(n):
    if graph[i]:
        now_node = i
        break

visited[now_node] = True
distance = 0
wait_list = []
print(graph)

while False in visited:
    nodes = graph[now_node]
    for node in nodes:
        wait_list.append(node)
    for node in wait_list:
        if node[1] < INF and visited[node[0]] == False:
            minimum_distance = node[1]
            minimum_node = node[0]
    visited[minimum_node] = True
    distance += minimum_distance
    now_node = minimum_node

print(distance)