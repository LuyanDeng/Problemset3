def quicksort2(arr, low, high, total_compare_count=0, total_swap_count=0):
    if low < high:
        pi, compare_count, swap_count = partition2(arr, low, high)
        total_compare_count += compare_count
        total_swap_count += swap_count

        # Recursively apply quicksort to the partitions
        total_compare_count, total_swap_count = quicksort2(arr, low, pi-1, total_compare_count, total_swap_count)
        total_compare_count, total_swap_count = quicksort2(arr, pi+1, high, total_compare_count, total_swap_count)

    # Only print and return the final counts at the top level call
    if low == 0 and high == len(arr) - 1:
        print("sorted array:", arr)
        print(f"total_compare_count: {total_compare_count}, total_swap_count: {total_swap_count}")
        return arr, total_compare_count, total_swap_count
    else:
        return total_compare_count, total_swap_count

def partition2(arr, low, high):
    pivot = arr[low]
    print(f"pivot: {pivot}")
    i = low + 1
    j = high
    compare_count = 0
    swap_count = 0
    print(f"i: {i}, j: {j}")
    while True:
        while i <= j and arr[i] <= pivot:
            i += 1
            compare_count += 1
            if i == high: break

        while i <= j and arr[j] > pivot:
            j -= 1
            compare_count += 1
            if j == low: break

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
            swap_count += 1
            print(f"Swapped {arr[j]} and {arr[i]}, arr: {arr}")
        else:
            break

    # Swap pivot with arr[j] if j has moved
    if j != low:
        arr[low], arr[j] = arr[j], arr[low]
        swap_count += 1
        print(f"Swapped pivot: {pivot} with {arr[low]}, arr: {arr}")

    print(f"Final partition: {arr}, compare_count: {compare_count}, swap_count: {swap_count}")
    print(f"arr[:{j}]: {arr[:j]}, arr[{j+1}:]: {arr[j+1:]}")
    return j, compare_count, swap_count
# arr = [5,4,9,8,3,7]
# arr = [2, 8,  7,  1, 3,  5,  6,  4]
arr = [1, 2, 3, 4, 5, 6, 7, 8]
# arr = [8, 7, 6, 5, 4, 3, 2, 1]
# arr = [8, 5, 3, 4, 2, 6, 1, 7]
quicksort2(arr,0,len(arr)-1)