nums = [5, 2, 9, 1, 5, 6]

def swap(arr, index_1, index_2):
    temp = arr[index_1]
    arr[index_1] = arr[index_2]
    arr[index_2] = temp

# define bubble_sort():
def bubble_sort(arr):
    # 2. A second loop is needed to itarate for each element
    for el in arr:
    # 1.can we use arr[:-1] One loop is only sufficent to move the largest element to its correct place
        for element in range(len(arr)-1):
          if arr[element] > arr[element + 1]:
            swap(arr, element, element + 1)





##### test statements

print("Pre-Sort: {0}".format(nums))
bubble_sort(nums)
print("Post-Sort: {0}".format(nums))
