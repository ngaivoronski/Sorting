# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    joined_arr = arrA + arrB
    for i in range(0, elements):
        minimum = min(joined_arr)
        joined_arr.remove(minimum)
        merged_arr[i] = minimum
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    if len(arr) == 0:
        return []
    # TO-DO
    list_of_arrs = [arr]

    # split the array in half until each sub-array is length 1
    while True:
        splits = 0
        new_list_of_arrs = []
        for i in list_of_arrs:
            if len(i) > 1:
                left = i[:len(i)//2]
                right = i[len(i)//2:]
                new_list_of_arrs.append(left)
                new_list_of_arrs.append(right)
                splits += 1
            else:
                new_list_of_arrs.append(i)
        if splits == 0:
            break
        else:
            list_of_arrs = new_list_of_arrs
    
    # merge sub arrays into sorted array
    while True:
        new_list_of_arrs = []
        last_element = []

        # if there's an odd number, remove the last element
        if len(list_of_arrs) % 2 > 0:
            last_element = list_of_arrs.pop()

        # merge pairs together
        for i in range(0, len(list_of_arrs), 2):
            new_list_of_arrs.append(merge(list_of_arrs[i], list_of_arrs[i+1]))

        # if last element was removed, add it back
        if last_element:
            new_list_of_arrs.append(last_element)

        # update the array
        list_of_arrs = new_list_of_arrs

        # if the updated array is length 1, stop the loop
        if len(list_of_arrs) == 1:
            break
    
    return list_of_arrs[0]



# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
