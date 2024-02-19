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
# arr = [26, 15, 10, 35, 29, 17, 22]
# arr = [2, 8,  7,  1, 3,  5,  6,  4]
# arr = [1, 2, 3, 4, 5, 6, 7, 8]
# arr = [8, 7, 6, 5, 4, 3, 2, 1]
arr = [8, 5, 3, 4, 2, 6, 1, 7]

# Generate a random integer array of size 100,000 elements
import random
# random_array = [random.randint(1, 100) for _ in range(100000)]
# # print(random_array)
# arr = random_array
# print("Original array:", arr)
# capture the start time
start = time.time()
heapSort(arr) # [1, 3, 4, 5, 10]

# print the running time
print(f"running time: {(time.time() - start) * 1000000}ms")
# print(f"running time: {(time.time() - start)}")