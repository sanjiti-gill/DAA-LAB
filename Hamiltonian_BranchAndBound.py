n = int(input("Enter number of vertices: "))

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

path = [0]

def isPromising(pos, v):
    if graph[path[-1]][v] == 0 or v in path:
        return False

    if pos < n - 1:
        for i in range(1, n):
            if i not in path and i != v:
                if not any(graph[i][j] == 1
                           for j in [0, v] + [
                               k for k in range(1, n)
                               if k not in path and k != v and k != i
                           ]):
                    return False

    return True

def hamiltonian(pos):
    if pos == n:
        if graph[path[-1]][0] == 1:
            print(path + [0])
        return

    for v in range(1, n):
        if isPromising(pos, v):
            path.append(v)
            hamiltonian(pos + 1)
            path.pop()

print("Hamiltonian cycles:")
hamiltonian(1)
