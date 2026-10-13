
n = int(input("Enter number of items: "))

profit = list(map(int, input("Enter profits: ").split()))
weight = list(map(int, input("Enter weights: ").split()))

capacity = int(input("Enter knapsack capacity: "))

ratio = []

for i in range(n):
    ratio.append(profit[i] / weight[i])

print("\nProfit-to-weight ratio:")
for i in range(n):
    print("Item", i + 1, ":", ratio[i])

items = list(range(n))
items.sort(key=lambda i: ratio[i], reverse=True)

total = 0

print("\nItem selection sequence:")

for i in items:
    if capacity >= weight[i]:
        capacity -= weight[i]
        total += profit[i]
        print("Item", i + 1, "- Fully selected")
    else:
        fraction = capacity / weight[i]
        total += profit[i] * fraction
        print("Item", i + 1, "- Fraction selected:", fraction)
        break

print("Maximum Profit:", total)
