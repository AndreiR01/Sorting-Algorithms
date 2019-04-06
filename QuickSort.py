from random import randrange, shuffle
#https://docs.python.org/3/library/random.html#random.randrange <-- Documentation
#QuickSort is a recursive algorithm, thus we will be having a base case and a recursive function
#We will sort our list in-place to keep it as efficient as possible. Sorting in-place means that we keep track of the sub-lists in our algorithm using pointers and swap values inside the list rather than create new lists
#Since doing this in-place, we will have two pointers:
    #1. Keep track of the "lesser than" values
    #2. Track progress throught the list.
    #HOW TO :
    #  # Create the lesser_than_pointer

        # Start a for loop, use 'idx' as the variable
            # Check if the value at idx is less than the pivot
                # If so:
                    # 1) swap lesser_than_pointer and idx values
                    # 2) increment lesser_than_pointer

  # After the loop is finished...
  # swap pivot with value at lesser_than_pointer
#Pointers are indicies that keep track of a portion of a list

def quicksort(list, start, end):
    #Base Case
    if start >= end:
        return list

    #select random element to be pivot
    pivot_idx = randrange(start, end + 1) #+1 in order to include last element
    pivot_element = list[pivot_idx]

    # Swapping the the random element with the last element of the list, pivot element will always be located at the end of the list.
    list[end], list[pivot_idx] = list[pivot_idx], list[end]

    #tracks all elements which should be to left(lesser than) pivot
    lesser_than_pointer = start

    for idx in range(start, end):
        #element out of place found
        if list[idx] < pivot_idx:
            #swap element to right-most portion of lesser elements
            list[lesser_than_pointer], list[idx] = list[idx], list[lesser_than_pointer]
            #tally that we have one lesser element
            lesser_than_pointer += 1
    #move pivot element to the right-most portion of lesser elements
    list[end], list[lesser_than_pointer] = list[lesser_than_pointer], list[end]

    #Calling quicksort on the left and right sub-lists
    quicksort(list, start, lesser_than_pointer - 1)
    quicksort(list, lesser_than_pointer + 1, end)


unsorted_list = [3,7,12,24,36,42]
shuffle(unsorted_list)
print(unsorted_list)
sorted_list = quicksort(unsorted_list, 0, len(unsorted_list)-1)
print(sorted_list)
