def is_safe(row, c):
    for r in range(row):
        if cols[r] == c or abs(cols[r] - c) == row - r:
            return False
    return True

def solve(row):
    global count
    
    if row == n:
        count += 1
        print("\nSolution", count)
        for r in range(n):
            print(". " * cols[r] + "Q " + ". " * (n - cols[r] - 1))
        return

    
    for c in range(n):
        if is_safe(row, c):
            print("  " * row + "Place Q at row", row, "col", c)
            cols[row] = c
            solve(row + 1)
            print("  " * row + "Backtrack from row", row, "col", c)


n = int(input("Enter N: "))
cols = [-1] * n
count = 0
solve(0)
print("\nTotal solutions:", count)
