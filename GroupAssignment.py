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
        # print("sorted array: ", arr)
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
            # print(f"Swapped {arr[i]} and {arr[j]}")
            arr[i], arr[j] = arr[j], arr[i]
            # increment the swap_count

            swap_count += 1
        # increment the compare_count
        compare_count += 1
    # when j reaches the end of the array, swap the pivot with the element at i+1
    # print(f"move pivot {arr[high]}to the right place: {arr[i + 1]}")
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    swap_count += 1
    # print(f"compare_count: {compare_count}")
    # print(f"swap_count: {swap_count}")
    # print(f"arr: {arr}")
    # print(f"pi: {arr[i + 1]}")
    return i + 1, compare_count, swap_count




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
            # print(f"Swapped {arr[j]} and {arr[i]}, arr: {arr}")
        else:
            break
    # print(f"swap pivot: {arr[low]} and {arr[j]}")
    if j != low:
        arr[low], arr[j] = arr[j], arr[low]
        swap_count += 1
    # print(f"Moved pivot to position {j}, arr: {arr}")
    # print(f"compare_count: {compare_count}, swap_count: {swap_count}")
    return j, compare_count, swap_count


#Write the Python code of Heapsort  Let your code compute and output the total number of comparisons,
# the total number of swaps, and the total running time

"""
heapsort using max heap
@:param arr: the input array
@:param total_compare_count: the total number of comparisons
@:param total_swap_count: the total number of swaps

"""
def heapify(arr, n, i,compare_count=0,swap_count=0):
    # n is the size of the heap, i is the index of the root of the subtree
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2


    # See if left child of root exists and is greater than root
    if l < n:
        compare_count += 1
        if arr[l] > arr[largest]:
            largest = l


    # See if right child of root exists and is greater than the largest so far
    if r < n :
        compare_count += 1
        if arr[r] > arr[largest]:
            largest = r


    # Change root, if needed
    if largest != i:
        # print(f"swap arr[i]: {arr[i]} arr[largest]: {arr[largest]}")
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
        swap_count += 1

        # Heapify the root.
        compare_count, swap_count = heapify(arr, n, largest, compare_count, swap_count)

    # print(f"compare_count: {compare_count}")
    # print(f"swap_count: {swap_count}")
    # print(f"arr after heapify: {arr}")
    return compare_count, swap_count

def buildMaxHeap(arr):
    n = len(arr)
    total_compare_count = 0
    total_swap_count = 0
    for i in range(n//2 - 1, -1, -1):
        compare_count, swap_count =heapify(arr, n, i)
        total_compare_count += compare_count
        total_swap_count += swap_count
    return total_compare_count, total_swap_count
def heapSort(arr):
    n = len(arr)

    # Build a maxheap.
    total_compare_count, total_swap_count = buildMaxHeap(arr)
    # print(f"arr after buildMaxHeap: {arr}")

    # One by one extract elements
    for i in range(n-1, 0, -1):
        # print(f"swap arr[i]: {arr[i]} arr[0]: {arr[0]}")
        arr[i], arr[0] = arr[0], arr[i]  # swap

        total_swap_count +=1
        compare_count, swap_count = heapify(arr, i, 0)
        total_compare_count += compare_count
        total_swap_count += swap_count
    print(f"total_compare_count: {total_compare_count}")
    print(f"total_swap_count: {total_swap_count}")
    return arr,total_compare_count, total_swap_count

import time
import random

import sys
sys.setrecursionlimit(1000000)
random_array = [random.randint(1, 100) for _ in range(100000)]
arr = random_array
# arr = [2, 8,  7,  1, 3,  5,  6,  4]
# arr = [1, 2, 3, 4, 5, 6, 7, 8]
# arr = [8, 7, 6, 5, 4, 3, 2, 1]
# arr = [8, 5, 3, 4, 2, 6, 1, 7]
#capture the start time
start = time.time()
quicksort1(arr, 0, len(arr) - 1)  # [1, 3, 4, 5, 10]
# # print the running time
print(f"running time: {(time.time() - start) }seconds")

start = time.time()
quicksort2(arr,0,len(arr)-1)

# print(f"running time: {(time.time() - start) * 1000000}ms")
# print the running time
print(f"running time: {(time.time() - start) }seconds")

start = time.time()
heapSort(arr) # [1, 3, 4, 5, 10]
#
# print the running time
print(f"running time: {(time.time() - start)}seconds")