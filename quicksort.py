import math

def partition(arr, left, right, pivot):
    print("Starting:", arr)
    i = left - 1
    j = left
    while j < right:
        if arr[j] > pivot:
            j += 1
            continue
        
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    print("Partitioned:", arr)
    
    pivot_index = i + 1
    arr.pop(right) 
    arr.insert(pivot_index, pivot)
    return pivot_index
            

def quicksort(arr, left, right):
    if (left >= right):
        return
    
    index = partition(arr, left, right, arr[right]) # Partition the array given the pivot which is the end of the list
    
    quicksort(arr, left, index - 1)
    quicksort(arr, index, right)



if __name__ == "__main__":
    arr = [59, 44, 2, 1, 4, 7, 9, 21, 36, 100, 99, 8, 12, 15, 13, 11, 85, 59, 99]
    quicksort(arr, 0, len(arr) - 1)
    print(arr)