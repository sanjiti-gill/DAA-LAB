
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = arr[:mid]
    right = arr[mid:]

    print("Dividing:", arr)

    left = merge_sort(left)
    right = merge_sort(right)

    merged = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged += left[i:]
    merged += right[j:]

    print("Merging:", merged)

    return merged


arr = list(map(int, input("Enter numbers: ").split()))

print("Original array:", arr)
arr = merge_sort(arr)
print("Sorted array:", arr)
