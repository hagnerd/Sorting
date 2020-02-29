def merge(arrA, arrB):
    merged_arr = []

    while len(arrA) > 0 and len(arrB) > 0:
        if arrA[0] < arrB[0]:
            merged_arr.append(arrA.pop(0))
        else:
            merged_arr.append(arrB.pop(0))

    merged_arr.extend(arrA)
    merged_arr.extend(arrB)

    return merged_arr

def merge_sort(arr):
    if len(arr) < 2:
        return arr

    half = len(arr) // 2
    left = merge_sort(arr[:half])
    right = merge_sort(arr[half:])

    return merge(left, right)


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r):
    # TO-DO
    if len(arr) < 2:
        return arr

    mid = (l + r) // 2

    return merge_in_place(arr, l, mid, r)


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
