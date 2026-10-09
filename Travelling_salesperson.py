
INF = float('inf')

def solve(mask, pos, dist, dp, parent, n):

    # All cities visited: return to city 0
    if mask == (1 << n) - 1:
        return dist[pos][0]

    # Return saved result if already calculated
    if dp[mask][pos] != -1:
        return dp[mask][pos]

    ans = INF
    best_next = -1

    # Try every unvisited city
    for city in range(n):
        if not (mask & (1 << city)):
            new_mask = mask | (1 << city)

            cost = dist[pos][city] + solve(
                new_mask, city, dist, dp, parent, n
            )

            if cost < ans:
                ans = cost
                best_next = city

    parent[mask][pos] = best_next
    dp[mask][pos] = ans

    return ans


# Input
n = int(input("Enter number of cities: "))

dist = []
print("Enter distance matrix row by row:")

for i in range(n):
    dist.append(list(map(int, input().split())))

# Initialise tables
dp = [[-1] * n for _ in range(1 << n)]
parent = [[-1] * n for _ in range(1 << n)]

# Calculate minimum cost
min_cost = solve(1, 0, dist, dp, parent, n)

# Reconstruct and display only the optimal route
path = [0]
mask = 1
pos = 0
total = 0

while parent[mask][pos] != -1:
    next_city = parent[mask][pos]
    cost = dist[pos][next_city]

    print(f"City {pos} -> City {next_city}: cost = {cost}")
    total += cost

    path.append(next_city)
    mask |= (1 << next_city)
    pos = next_city

# Return to starting city
print(f"City {pos} -> City 0: cost = {dist[pos][0]}")
path.append(0)

print("\nMinimum travelling cost:", min_cost)
print("Optimal path:", " -> ".join(map(str, path)))
