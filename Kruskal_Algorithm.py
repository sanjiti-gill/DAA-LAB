V = int(input("Enter number of vertices: "))

print("Enter adjacency matrix (0 if no edge):")
graph = []
for i in range(V):
    graph.append(list(map(int, input().split())))

edges = []

for i in range(V):
    for j in range(i + 1, V):
        if graph[i][j] != 0:
            edges.append((graph[i][j], i, j))

edges.sort()

parent = list(range(V))
cost = 0
count = 0

print("Selected edges:")

for w, u, v in edges:
    a, b = u, v

    while parent[a] != a:
        a = parent[a]
    while parent[b] != b:
        b = parent[b]

    if a != b:
        print(u, "-", v, ":", w)
        cost += w
        parent[a] = b
        count += 1

        if count == V - 1:
            break

print("Minimum Cost:", cost)
