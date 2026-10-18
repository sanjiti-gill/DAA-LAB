
n = int(input("Enter number of activities: "))

activities = []

for i in range(n):
    start = int(input("Enter start time: "))
    finish = int(input("Enter finish time: "))
    activities.append((start, finish))

# Sort activities by finishing time
activities.sort(key=lambda x: x[1])

print("\nActivities sorted by finishing time:")
print(activities)

# Select compatible activities
selected = []
last_finish = 0

for activity in activities:
    if activity[0] >= last_finish:
        selected.append(activity)
        last_finish = activity[1]

print("\nSelected compatible activities:")
print(selected)

print("Maximum number of activities:", len(selected))
