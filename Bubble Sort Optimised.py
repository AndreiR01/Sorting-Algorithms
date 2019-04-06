
# nums = [5, 4, 3, 2, 1]
# 5 element list: N is 5
#bubble_sort(nums)
# Consider the 1st pass throught the outer loop.
# 5 > 4
# [4, 5, 3, 2, 1]
# 5 > 3
# [4, 3, 5, 2, 1]
# 5 > 2
# [4, 3, 2, 5, 1]
# 5 > 1
# [4, 3, 2, 1, 5]
# four comparisons total
# We now know last value is in its correct position, as a result we do not need to worry about it. The second time throguth the loop we only need n-2 comparisons
# An optimised version doesnt make N^2 comparisons but (n-1) + (n-2) + ... + 2 + 1. It can be simplified to (N^2 - N)/ 2 . This is fewer than N^2 - N but still O(N^2)

nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print("PRE SORT: {0}".format(nums))

def swap(arr, index_1, index_2):
    temp = arr[index_1]
    arr[index_1] = arr[index_2]
    arr[index_2] = temp

def bubble_sort_unoptimized(arr):
    iterations = 0
    for el in arr:
        for index in range(len(arr) - 1):
            iterations += 1
        if arr[index] > arr[index + 1]:
            swap(arr, index, index + 1)

    print("PRE-OPTIMIZED ITERATION COUNT: {0}".format(iterations))

def bubble_sort(arr):
    iterations = 0
    for i in range(len(arr)):
        # iterate through unplaced elements
        # By reducing the inner loop in relation to the number of iterations in the outer loop, we avoid iterating over elements which are correctly placed.
        for idx in range(len(arr) - i - 1):
            iterations += 1
            if arr[idx] > arr[idx + 1]:
                # replacement for swap function by taking advantage of parallel assignment.
                arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]

    print("POST-OPTIMIZED ITERATION COUNT: {0}".format(iterations))

bubble_sort_unoptimized(nums.copy())
bubble_sort(nums)
print("POST SORT: {0}".format(nums))
