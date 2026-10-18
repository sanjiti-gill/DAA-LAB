
V = int(input("Enter number of vertices: "))
E = int(input("Enter number of edges: "))

edges = []

print("Enter edges (u v weight):")
for i in range(E):
    u, v, w = map(int, input().split())
    edges.append((w, u, v))

edges.sort()

parent = list(range(V))
cost = 0

print("Selected edges:")

for w, u, v in edges:
    a = u
    b = v

    while parent[a] != a:
        a = parent[a]

    while parent[b] != b:
        b = parent[b]

    if a != b:
        print(u, "-", v, ":", w)
        cost += w
        parent[a] = b

print("Minimum Cost:", cost)
