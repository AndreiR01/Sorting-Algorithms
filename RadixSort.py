#O(wn)-O(n)- as long as the length of list is larger than the number of digits
#w - number of digits
#n- input list of length n
def radix_sort(to_be_sorted):
    maximum_value = max(to_be_sorted)
    max_exponent = len(str(maximum_value))
    #creating a copy in order to not mutate the input list
    being_sorted = to_be_sorted[:]
    #iterating for the max number of digits within the input(W)
    for exponent in range(max_exponent):
        #position variable keeps track of which exponent we are looking at. exponent is zero-indexed our position is going to be one more than the exponent
        position = exponent + 1
        #indexing the string in reverse thus -position
        index = -position
        #creating 10 different "buckets" since we have 10 different value (0 through 9)
        digits = [[] for i in range(10)]

        #selecting the digit at the current iteration index and placing it in the correct bucket
        #iterating for each element in the input(N)
        for number in being_sorted:
            #turning the number to a string in order to access the last element
            number_as_a_string = str(number)
            try:
                #retrieving the single digit stored at this iteration
                digit = number_as_a_string[index]
            except IndexError:
                digit = 0

            #digit needs to be an integer in order to use digit as a list index for digits
            digit = int(digit)
            digits[digit].append(number)

        # all our input numbers are in digits we will clear our being_sorted
        being_sorted = []
        #Loop iterating throught each of our lists in digits

        for numeral in digits:#numeral since each list represents a number bucket
            being_sorted.extend(numeral)#extend appends all the elements of a list as apposed to appending the list itself.
    return being_sorted

unsorted_list = [830, 921, 163, 373, 961, 559, 89, 199, 535, 959, 40, 641, 355, 689, 621, 183, 182, 524, 1]
print(radix_sort(unsorted_list))
