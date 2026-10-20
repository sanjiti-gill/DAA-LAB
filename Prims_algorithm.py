n = int(input("Enter number of vertices: "))

print("Enter adjacency matrix (0 if no edge):")
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

visited = [False] * n
visited[0] = True
cost = 0

print("Selected edges:")

for _ in range(n - 1):
    minimum = float('inf')

    for i in range(n):
        for j in range(n):
            if visited[i] and not visited[j] and graph[i][j] != 0:
                if graph[i][j] < minimum:
                    minimum = graph[i][j]
                    u, v = i, j

    visited[v] = True
    cost += minimum
    print(u, "-", v, ":", minimum)

print("Minimum Cost:", cost)
