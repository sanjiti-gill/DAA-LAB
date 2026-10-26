def is_safe(v, c):
    for u in range(n):
        if graph[v][u] == 1 and colors[u] == c:
            return False
    return True

def solve(v, m):
    if v == n:
        return True
    for c in range(1, m + 1):
        if is_safe(v, c):
            colors[v] = c
            if solve(v + 1, m):
                return True
            colors[v] = 0   # backtrack
    return False

n = int(input("Enter number of vertices: "))
graph = []
print("Enter adjacency matrix (0/1), row by row:")
for i in range(n):
    graph.append(list(map(int, input().split())))

for m in range(1, n + 1):
    colors = [0] * n
    if solve(0, m):
        print("Minimum colors needed:", m)
        for v in range(n):
            print("Vertex", v, "-> Color", colors[v])
        break
