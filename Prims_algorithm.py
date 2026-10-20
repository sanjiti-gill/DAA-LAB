
V = int(input("Enter number of vertices: "))

print("Enter adjacency matrix (0 if no edge):")
graph = []
for i in range(V):
    graph.append(list(map(int, input().split())))

visited = [False] * V
visited[0] = True
cost = 0

print("Selected edges:")

for _ in range(V - 1):
    minimum = float('inf')

    for i in range(V):
        for j in range(V):
            if visited[i] and not visited[j] and graph[i][j] != 0:
                if graph[i][j] < minimum:
                    minimum = graph[i][j]
                    u, v = i, j

    visited[v] = True
    cost += minimum
    print(u, "-", v, ":", minimum)

print("Minimum Cost:", cost)
