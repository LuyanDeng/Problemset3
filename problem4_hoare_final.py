from random import random


def hoare_partition(arr, low, high):
    pivot = arr[low]
    i = low - 1
    j = high + 1
    local_comparison_count = 0
    local_swap_count = 0

    while True:
        i += 1
        while arr[i] < pivot:
            i += 1
            local_comparison_count += 1

        j -= 1
        while arr[j] > pivot:
            j -= 1
            local_comparison_count += 1

        if i >= j:
            return j, local_comparison_count, local_swap_count

        # Swap when elements are not in the order
        arr[i], arr[j] = arr[j], arr[i]
        local_swap_count += 1


def quick_sort_hoare(arr, low, high, current_comparison_count=0, current_swap_count=0):
    if low < high:
        p, local_comparison_count, local_swap_count = hoare_partition(arr, low, high)
        new_comparison_count = current_comparison_count + local_comparison_count
        new_swap_count = current_swap_count + local_swap_count

        # Left side of the pivot
        new_comparison_count, new_swap_count = quick_sort_hoare(arr, low, p, new_comparison_count, new_swap_count)

        # Right side of the pivot
        new_comparison_count, new_swap_count = quick_sort_hoare(arr, p + 1, high, new_comparison_count, new_swap_count)

        return new_comparison_count, new_swap_count
    else:
        return current_comparison_count, current_swap_count


def quick_sort_entry(arr):
    final_comparison_count, final_swap_count = quick_sort_hoare(arr, 0, len(arr) - 1)
    print("Total number of comparisons:", final_comparison_count)
    print("Total number of swaps:", final_swap_count)

import time
# Driver/test code
arr = [2, 8,  7,  1, 3,  5,  6,  4]

# arr = [1, 2, 3, 4, 5, 6, 7, 8]
# arr = [8, 7, 6, 5, 4, 3, 2, 1]
# arr = [8, 5, 3, 4, 2, 6, 1, 7]
import random
import sys
# sys.setrecursionlimit(1000000)
# random_array = [random.randint(1, 100) for _ in range(100000)]
# arr = random_array
print("------------------------")
print("quicksort_hoare")
start = time.time()
quick_sort_entry(arr)
# print the running time
print(f"running time: {(time.time() - start) * 1000000}")
# print(f"running time: {(time.time() - start)}seconds")
