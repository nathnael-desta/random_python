unsorted = [22, 11, 88, 66, 55, 77, 33, 44]

def quick_sort(arr, final = []):
    if len(arr) == 1 or arr == []:
        return arr
    left_arr, pivot, right_arr = sort_pivot(arr)
    # print(arr, sort_pivot(arr))
    # print(arr, left_arr, pivot, right_arr)
    return quick_sort(left_arr) + [pivot] + quick_sort(right_arr)



def sort_pivot(orig_arr):
    arr = orig_arr[:]
    l, r, p = 0, len(arr) - 2 ,len(arr) - 1
    if p == 0:
        return [], arr, []
    while True:
        while arr[l] < arr[p] and l < p:
            l += 1
        while arr[r] > arr[p] and 0 < r:
            r -= 1
        if r <= l:
            break
        arr[r], arr[l] = arr[l], arr[r]
    
    arr[p], arr[l] = arr[l], arr[p]
    print(arr , l)

    return split(arr, l)


def split(arr, p):
    if len(arr) == 0:
        return [], arr[p], []
    left_arr = arr[0:p]
    right_arr = arr[p + 1:] if p + 1 < len(arr) else []
    # print(right_arr)
    # print(arr, left_arr, arr[p], right_arr)
    return left_arr, arr[p], right_arr

print(quick_sort(unsorted))
# print(split([11, 22], 0))

# print(sort_pivot([11, 22]))

# print([11,22][1:])