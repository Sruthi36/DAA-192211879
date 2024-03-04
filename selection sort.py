def selection_sort(array,size):
    for i in range(size):
        min_index = i
        for j in range(i+1,size):
            if array[j] < array[min_index]:
                min_index = j
        array[i],array[min_index] = array[min_index],array[i]
array = [-1,45,0,11,-9]
selection_sort(array,len(array))
print(array)
