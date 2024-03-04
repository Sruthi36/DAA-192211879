def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left_half = arr[:mid]
    right_half = arr[mid:]
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    return merge(left_half,right_half)
def merge(left_arr,right_arr):
    sorted_arr = []
    left_index = 0
    right_index = 0
    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            sorted_arr.append(left_arr[left_index])
            left_index += 1
        else:
            sorted_arr.append(right_arr[right_index])
            right_index += 1
    sorted_arr.extend(left_arr[left_index:])
    sorted_arr.extend(right_arr[right_index:])
    print(sorted_arr)
    return sorted_arr
array = [10,3,11,2,1]
sorted_array = merge_sort(array)
print(sorted_array)
