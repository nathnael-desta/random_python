myarr = [22, 11]

def bubble_sort(arr, l, r, p):
    new_pivot = bubble_sort_lap(arr, l, r, p)
    if p - new_pivot > 1:
        bubble_sort(arr, new_pivot + 1, p - 1, p)
    if new_pivot - l > 1:
        bubble_sort(arr, l, new_pivot - 2, new_pivot - 1 )

def bubble_sort_lap(arr, l, r, p):
    while True:
        while arr[l] <= arr[p] and l < p:
            l += 1
        while arr[r] >= arr[p] and r > 0:
            r -= 1
        if l >= r:
            break
        arr[l], arr[r] = arr[r], arr[l]
    arr[l], arr[p] = arr[p], arr[l]
    return l




print(bubble_sort(myarr, 0 , len(myarr) - 2, len(myarr) - 1))
print(myarr)

# print(bubble_sort_lap([22, 11, 33], 0 , 1, 2))
