def bubble_sort(array):
    n = len(array)
    swapped = False
    for i in range(n-1):
        for j in range(0,n-i-1):
            if array[j] > array[j+1]:
                swapped = True
                array[j],array[j+1] = array[j+1],array[j]
    if not swapped:
        return
array = [3,9,1,12,22,11]
bubble_sort(array)
print(array)
