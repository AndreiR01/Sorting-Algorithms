# separates the input list into parts
def merge_sort(items):
    #base case
    if len(items) <= 1:
        return items
    #list passed in will be split into half and assigned to left and right split
    middle_index = len(items) // 2
    left_split = items[:middle_index]
    right_split = items[middle_index:]
    #recursive function
    left_sorted = merge_sort(left_split)
    right_sorted = merge_sort(right_split)

    return merge(left_sorted, right_sorted)

#helper function which joins the data up.
def merge(left, right):

    result = []
    # While loop which runs until there is a left and a right
    while(left and right):
        if left[0] < right[0]:
            result.append(left[0])# SInce we are choosing the smaller of the two
            left.pop(0)# We added the 1st elem so we need to remove it
        elif left[0] > right[0]:
            result.append(right[0])
            right.pop(0)
    #after while loop we depleated on eof out inputs, now add in the rest of the value to finish off the merge
    if left:
        result += left
    if right:
        result += right
    #returning the sorted list
    return result

#TESTING-------
unordered_list1 = [356, 746, 264, 569]
orderded_list1 = merge_sort(unordered_list1)
print("Undordered list 1:\n" + str( unordered_list1))
print("Ordered list 1:\n" + str(orderded_list1))

unordered_list2 = [787, 677, 391, 318, 543, 717, 180, 113, 795, 19, 202, 534, 201, 370, 276, 975, 403, 624, 770, 595, 571, 268, 373]
ordered_list2 = merge_sort(unordered_list2)
print("Undordered list 2:\n" + str(unordered_list2))
print("Ordered list 2:\n" + str(ordered_list2))

unordered_list3 = [860, 380, 151, 585, 743, 542, 147, 820, 439, 865, 924, 387]
ordered_list3 = merge_sort(unordered_list3)
print("Undordered list 3:\n" + str(unordered_list3))
print("Ordered list 3:\n" + str(ordered_list3))
#------------
