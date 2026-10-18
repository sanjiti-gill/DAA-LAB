
comparisons = 0
swaps = 0

def quick_sort(arr, low, high):
    global comparisons, swaps

    if low < high:
        pivot = arr[high]
        print("Pivot:", pivot)

        i = low - 1

        for j in range(low, high):
            comparisons += 1

            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                swaps += 1

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        swaps += 1

        p = i + 1
        print("After partition:", arr)

        quick_sort(arr, low, p - 1)
        quick_sort(arr, p + 1, high)


arr = list(map(int, input("Enter numbers: ").split()))

quick_sort(arr, 0, len(arr) - 1)

print("Sorted array:", arr)
print("Comparisons:", comparisons)
print("Swaps:", swaps)
