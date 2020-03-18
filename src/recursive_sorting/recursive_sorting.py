# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    for i in range(0, elements):
        if len(arrA) == 0:
            merged_arr[i] = arrB[0]
            arrB.remove(arrB[0])
        elif len(arrB) == 0:
            merged_arr[i] = arrA[0]
            arrA.remove(arrA[0])
        elif arrA[0] > arrB[0]:
            merged_arr[i] = arrB[0]
            arrB.remove(arrB[0])
        else:
            merged_arr[i] = arrA[0]
            arrA.remove(arrA[0])
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    if len(arr) > 1:
        # split the array into two sub-arrays
        left = arr[:len(arr)//2]
        right = arr[len(arr)//2:]

        # recursivley run function on subarrays
        l = merge_sort(left)
        r = merge_sort(right)

        # merge left and right subfunctions
        return merge(l, r)
    else:
        return arr







# STRETCH: implement an in-place  merge sort algorithm
def merge_in_place(arrA, arrB, arrM=[]):
    arrM = [0] * (len( arrA ) + len( arrB ))
    # TO-DO
    for i in range(0, len(arrM)):
        if len(arrA) == 0:
            arrM[i] = arrB[0]
            arrB.remove(arrB[0])
        elif len(arrB) == 0:
            arrM[i] = arrA[0]
            arrA.remove(arrA[0])
        elif arrA[0] > arrB[0]:
            arrM[i] = arrB[0]
            arrB.remove(arrB[0])
        else:
            arrM[i] = arrA[0]
            arrA.remove(arrA[0])
    return arrM

def merge_sort_in_place(arr, l=[], r=[]): 
    # TO-DO
    if len(arr) > 1:
        # split the array into two sub-arrays
        l = arr[:len(arr)//2]
        r = arr[len(arr)//2:]

        # merge left and right subfunctions
        return merge_in_place(merge_sort_in_place(l), merge_sort_in_place(r))
    else:
        return arr

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
