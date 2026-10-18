
n=int(input("enter no. of items: "))

profit=[]
weight=[]
ratio=[]

print("Enter profits: ")
for i in range(n):
    profit.append(int(input()))

print("Enter weights: ")
for i in range(n):
    weight.append(int(input()))

for i in range(n):
    ratio.append(profit[i]/weight[i])


capacity=int(input("Enter capacity of knapsack: "))

print("PROFIT TO WEIGHT RATIOS: ")
for i in range(n):
    print("Item", i+1, ":", ratio[i])


items=list(range(n))
items.sort(key= lambda i: ratio[i], reverse=True)

total=0

print("\nItem selection sequence: ")

for i in items:
    if capacity>=weight[i]:
        capacity-=weight[i]
        total+=profit[i]
        print("Item", i+1, "- fully selected")
    else:
        fraction=capacity/weight[i]
        total+=profit[i]*fraction
        print("Item", i+1, "-fraction selected: ", fraction)

print("Maximum profit: ", total)




