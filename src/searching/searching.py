# STRETCH: implement Linear Search				
def linear_search(arr, target):
  
  # TO-DO: add missing code
  for i in range(0, len(arr)):
    if arr[i] == target:
      return i

  return -1   # not found


# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):

  if len(arr) == 0:
    return -1 # array empty

  # TO-DO: add missing code
  temp = arr
  index = 0
  while True:
    if len(temp) == 1:
      if temp[0] == target:
        return index
      else:
        return -1
    
    left = temp[:len(temp)//2]
    right = temp[len(temp)//2:]

    if left[-1] < target:
      temp = right
      index += len(left)
    elif left[-1] > target:
      temp = left
    else:
      return index + len(left) - 1

  return -1 # not found


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high, index=0):
  if len(arr) == 0:
    return -1 # array empty
  # TO-DO: add missing if/else statements, recursive calls

  if len(arr) > 1:
    left = arr[:len(arr)//2]
    right = arr[len(arr)//2:]
    if left[-1] < target:
      new_index = index + len(left)
      return binary_search_recursive(right, target, low, high, new_index)
    elif left[-1] > target:
      return binary_search_recursive(left, target, low, high, index)
    else:
      return index + len(left) - 1
  else:
    return index
