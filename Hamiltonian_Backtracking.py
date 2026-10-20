n = int(input("Enter number of vertices: "))

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

path = [0]

def hamiltonian(pos):
    if pos == n:
        if graph[path[-1]][path[0]] == 1:
            print(path + [path[0]])
        return

    for v in range(1, n):
        if v not in path and graph[path[-1]][v] == 1:
            path.append(v)
            hamiltonian(pos + 1)
            path.pop()

print("Hamiltonian cycles:")
hamiltonian(1)
