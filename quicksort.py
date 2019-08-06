import math

def partition(arr, left, right, pivot):
    print("    Partitioning", arr[left:right], "With " + str(pivot))
    while (left <= right):
        while (arr[left] < pivot):
            left += 1

        while (arr[right] > pivot):
            right -= 1
        
        while left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    
    return left

def quicksort(arr, left, right):
    print(arr, left, right)
    if (left >= right):
        return
    
    pv_n = int((left + right) / 2)
    pivot = arr[pv_n]
    index = partition(arr, left, right, pivot)

    quicksort(arr, left, index - 1)
    quicksort(arr, index, right)



if __name__ == "__main__":
    arr = [10, 3, 5, 11, 12, 4]
    quicksort(arr, 0, len(arr) - 1)
    print(arr)