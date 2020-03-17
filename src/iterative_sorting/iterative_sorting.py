# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for x in range(i, len(arr)):
            if arr[x] < arr[smallest_index]:
                smallest_index = x
        
        # TO-DO: swap
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    while True:
        # reset change count
        changes = 0
        for i in range(0, len(arr) - 1):
            # swap numbers in pair if i+1 is less than i, add 1 to the change count
            if arr[i+1] < arr[i]:
                arr[i+1], arr[i] = arr[i], arr[i+1]
                changes += 1
        # if there have been no changes on the previous pass, stop the algorithm
        if changes == 0:
            break

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr ):
    # if empty array, return empty array
    if arr == []:
        return []
    # if there are negative numbers, return an error
    if min(arr) < 0:
        return "Error, negative numbers not allowed in Count Sort"

    # get the minimum / maximum
    minimum = min(arr)
    maximum = max(arr)

    # set a new empty dictionary
    count_dict = {}

    # create a dictionary element for each number minimum -> maximum
    for i in range(minimum, maximum + 1):
        count_dict[i] = 0
        # count how many times that number appears in the array and set that to the "value"
        for x in range(0, len(arr)):
            if arr[x] == i:
                count_dict[i] += 1
    
    # set up sorted array
    sorted_arr = []

    # add each "key" of count_dict to sorted_arr its "value" times
    for i in count_dict.keys():
        if count_dict[i] > 0:
            for x in range(0,count_dict[i]):
                sorted_arr.append(i)

    return sorted_arr