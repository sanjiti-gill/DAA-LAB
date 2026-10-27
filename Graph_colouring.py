def is_safe(v, c):
    for i in range(v):
        if graph[v][i] == 1 and color[i] == c:
            return False
    return True

def solve(v, m):
    if v == n:
        return True

    for c in range(1, m + 1):
        if is_safe(v, c):
            color[v] = c

            if solve(v + 1, m):
                return True

            color[v] = 0

    return False

n = int(input("Enter number of vertices: "))

print("Enter adjacency matrix:")
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

color = [0] * n

for m in range(1, n + 1):
    if solve(0, m):
        print("\nMinimum colors required:", m)
        print("Valid color assignment:")

        for i in range(n):
            print("Vertex", i, ":", "Color", color[i])

        break
