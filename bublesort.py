myarr = [9, 1, 8, 2, 7, 3, 6, 4, 5]


def bubble_sort(arr):
    for i in range(len(arr)):
        print("temp", arr)
        noswap = True
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                noswap = False
        if noswap:
            break
    return arr


print(bubble_sort(myarr))
