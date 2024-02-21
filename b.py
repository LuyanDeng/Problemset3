# Write the Python code of the Hoare implementation of quicksort
# Let your code compute and output the total number of comparisons, the total number of swaps, and the total running time.

"""
quick sort using Hoare method
@:param arr: the input array
"""
def quicksort2(arr, low, high, total_compare_count=0, total_swap_count=0):
    if low < high:
        pi, compare_count, swap_count = partition2(arr, low, high)
        total_compare_count += compare_count
        total_swap_count += swap_count

        total_compare_count, total_swap_count = quicksort2(arr, low, pi-1, total_compare_count, total_swap_count)
        total_compare_count, total_swap_count = quicksort2(arr, pi + 1, high, total_compare_count, total_swap_count)

    if low == 0 and high == len(arr) - 1:
        # print("sorted array: ", arr)
        print(f"total_compare_count: {total_compare_count}")
        print(f"total_swap_count: {total_swap_count}")
        return arr, total_compare_count, total_swap_count
    else:
        return total_compare_count, total_swap_count


"""
partition the array using Hoare method, set the pivot as the first element of the array
and set the left pointer as the first element of the array and the right pointer as the last element of the array
move the left pointer to the right , and find the element less than pivot
move the right pointer to the left, and find the element greater than pivot
swap those two elements
@:param arr: the input array
@:param low: the first index of the array
@:param high: the last index of the array
@ return: the partition index of the array
@ return: the number of comparisons
@ return: the number of swaps
"""
def partition2(arr,low,high):
    # set the pivot as the first element of the array
    pivot = arr[low]
    # print(f"pivot: {pivot}")
    # initialize the i as left pointer and j as right pointer
    i = low+1
    j = high
    # initialize the compare_count and swap_count
    compare_count = 0
    swap_count = 0
    # iterate through the array
    # print(f"i: {i}")
    while True:
        # Move right pointer until finding an element greater than the pivot
        while i <= j and arr[i] <= pivot:
            i += 1
            compare_count += 1
            if i == high: break  # Break if i reaches the end

        # Move left pointer until finding an element less than the pivot
        while i <= j and arr[j] > pivot:
            j -= 1
            compare_count += 1
            if j == low: break  # Break if j reaches the start

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
            swap_count += 1
            print(f"Swapped {arr[j]} and {arr[i]}, arr: {arr}")
        else:
            break
    if j != low:
        arr[low], arr[j] = arr[j], arr[low]
        swap_count += 1
        print(f"Swapped pivot: {pivot} with {arr[low]}, arr: {arr}")

    print(f"Final partition: {arr}, compare_count: {compare_count}, swap_count: {swap_count}")
    # print(f"arr[:{j}]: {arr[:j]}, arr[{j + 1}:]: {arr[j + 1:]}")
    return j, compare_count, swap_count

import time
# arr = [5,4,9,8,3,7]
arr = [2, 8,  7,  1, 3,  5,  6,  4]
# arr = [1, 2, 3, 4, 5, 6, 7, 8]
# arr = [8, 7, 6, 5, 4, 3, 2, 1]
# arr = [8, 5, 3, 4, 2, 6, 1, 7]
# from heapsort import random_array
# arr = random_array
# print("Original array:", arr)
# capture the start time
start = time.time()
quicksort2(arr,0,len(arr)-1) # [1, 3, 4, 5, 10]

# print the running time
print(f"running time: {(time.time() - start) * 1000}ms")