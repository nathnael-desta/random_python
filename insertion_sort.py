my_arr = [4,5,2,3,4,1,9,0,7,8,5]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        for j in range (i - 1, -1, -1):
            if arr[j] >= temp:
                arr[j + 1] = arr[j]
            else:
                arr[j + 1] = temp
                break
            if j == 0:
                arr[0] = temp

    return arr

print(insertion_sort(my_arr))