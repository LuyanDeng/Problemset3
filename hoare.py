def partition2(arr, low, high):
    pivot = arr[low]
    i = low + 1  # Start from the next element after pivot
    j = high
    compare_count = 0
    swap_count = 0

    while True:
        # Move right until element > pivot or i crosses j
        while i <= j and arr[i] <= pivot:
            i += 1
            compare_count += 1
        # Move left until element < pivot or j crosses i
        while i <= j and arr[j] > pivot:
            j -= 1
            compare_count += 1
        if i < j:
            print(f"Swapped {arr[j]} and {arr[i]}")
            arr[i], arr[j] = arr[j], arr[i]
            swap_count += 1
            i += 1  # Increment i to continue scanning from the next position
            j -= 1  # Decrement j to continue scanning from the previous position
        else:
            break

    arr[low], arr[j] = arr[j], arr[low]  # Swap pivot into correct position

    swap_count += 1
    print(f"compare_count: {compare_count}, swap_count: {swap_count}")
    return j, compare_count, swap_count


def quicksort2(arr, low, high, total_compare_count=0, total_swap_count=0):
    if low < high:
        pi, compare_count, swap_count = partition2(arr, low, high)
        total_compare_count += compare_count
        total_swap_count += swap_count

        total_compare_count, total_swap_count = quicksort2(arr, low, pi-1, total_compare_count, total_swap_count)
        total_compare_count, total_swap_count = quicksort2(arr, pi + 1, high, total_compare_count, total_swap_count)

    if low == 0 and high == len(arr) - 1:
        return arr, total_compare_count, total_swap_count
    else:
        return total_compare_count, total_swap_count


# Example usage
arr = [5,4,9,8,3,7]
print("Original array:", arr)
sorted_array, total_compare_count, total_swap_count = quicksort2(arr, 0, len(arr) - 1,0,0)
print("Sorted array:", sorted_array)
print(f"Total comparisons: {total_compare_count}, Total swaps: {total_swap_count}")
