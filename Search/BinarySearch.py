def isArrSorted (arr):
    for i in range (0, len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

def binary_search (arr, item):

    if isArrSorted (arr) == False:
        return None
    
    if item == arr[0]:
        return 0

    low = 0
    high = len(arr) - 1
    
    while low != high:

        mid = round((low + high) / 2)

        if item == arr[mid]:
            return mid

        elif item < arr[mid]:
            high = mid

        elif item > arr[mid]: 
            low = mid

    return None


array = [1,1]

print (binary_search(array,1))
