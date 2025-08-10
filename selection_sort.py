my_arr = [4,5,2,3,4,1,9,0,7,8,5]

def selection_sort(arr):
    for i in range(len(arr) - 1):
        smallest = arr[i]
        smallest_ind = i
        for j in range(i + 1, len(arr)):
            if smallest > arr[j]:
                smallest = arr[j]
                smallest_ind = j
        arr[i], arr[smallest_ind] = arr[smallest_ind], arr[i]
    return arr
            
print(selection_sort(my_arr))