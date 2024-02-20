# Problem 4:

# a)
# Write the Python code of Quicksort, using the Lomuto method as we saw in class (the pivot is always
# the last (right-most) element of the input array). Clearly document your code so that it is clear how your
# algorithm works. Let your code compute and output the total number of comparisons, the total number of swaps,
# and the total running time.
# If the running time is too small, multiply it by 1,000,000 (or higher power of 10) before printing it
"""

@:param arr: the input array
@:param low: the lower index of the array
@:param high: the higher index of the array
@:param total_compare_count: the total number of comparisons
@:param total_swap_count: the total number of swaps
@:return: the sorted array
@:return: the total number of comparisons
@:return: the total number of swaps
"""


def quicksort1(arr, low, high, total_compare_count=0, total_swap_count=0):
    if low < high:
        # pi is partitioning index, arr[p] is now at the right place
        pi, compare_count, swap_count = partition1(arr, low, high)
        total_compare_count += compare_count
        total_swap_count += swap_count
        # print(f"compare_count: {compare_count}")
        # print(f"swap_count: {swap_count}")

        # Separately sort elements before partition and after partition
        total_compare_count, total_swap_count = quicksort1(arr, low, pi - 1, total_compare_count, total_swap_count)
        total_compare_count, total_swap_count = quicksort1(arr, pi + 1, high, total_compare_count, total_swap_count)
    if low == 0 and high == len(arr) - 1:
        print("sorted array: ", arr)
        print(f"total_compare_count: {total_compare_count}")
        print(f"total_swap_count: {total_swap_count}")
        return arr, total_compare_count, total_swap_count
    else:
        return total_compare_count, total_swap_count


"""
Partition the array using Lomuto Partition Method, the pivot is always the last (right-most) element of the input array.

@:param arr: the input array
@:param low: the lower index of the array
@:param high: the higher index of the array
@:return: the partition index of the array
@:return: the number of comparisons
@:return: the number of swaps
"""


def partition1(arr, low, high):
    # set the pivot as the last element of the array

    pivot = arr[high]
    # print(f"pivot: {pivot}")

    i = low - 1
    # initialize the compare_count and swap_count
    compare_count = 0
    swap_count = 0
    # iterate through the array
    for j in range(low, high):
        # if the current element is less than the pivot, index i move right one step,
        # and swap the current element with the element at ith
        if arr[j] < pivot:
            i += 1
            print(f"Swapped {arr[i]} and {arr[j]}")
            arr[i], arr[j] = arr[j], arr[i]
            # increment the swap_count

            swap_count += 1
        # increment the compare_count
        compare_count += 1
    # when j reaches the end of the array, swap the pivot with the element at i+1
    print(f"move pivot {arr[high]}to the right place: {arr[i + 1]}")
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    swap_count += 1
    # print(f"compare_count: {compare_count}")
    # print(f"swap_count: {swap_count}")
    # print(f"arr: {arr}")
    # print(f"pi: {arr[i + 1]}")
    return i + 1, compare_count, swap_count


import time

# arr = [5, 4, 9, 8, 3, 7]
# arr = [2, 8,  7,  1, 3,  5,  6,  4]
arr = [1, 2, 3, 4, 5, 6, 7, 8]
# arr = [8, 7, 6, 5, 4, 3, 2, 1]
# arr = [8, 5, 3, 4, 2, 6, 1, 7]

# capture the start time
start = time.time()
# call the quicksort1 function
quicksort1(arr, 0, len(arr) - 1)
# print the running time
print(f"running time: {(time.time() - start) * 1000000}ms")
# print(sum(arr))
