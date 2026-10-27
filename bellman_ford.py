V = int(input("Enter number of vertices: "))
E = int(input("Enter number of edges: "))

print("Enter each edge as: from to weight")
edges = []
for _ in range(E):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))

source = int(input("Enter source vertex: "))

dist = [float('inf')] * V
dist[source] = 0

for i in range(V - 1):
    for u, v, w in edges:
        if dist[u] + w < dist[v]:
            dist[v] = dist[u] + w
    print(f"Iteration {i + 1}: {dist}")

print("\nShortest distances from source", source)
for i in range(V):
    print(f"{source} -> {i} : {dist[i]}")
