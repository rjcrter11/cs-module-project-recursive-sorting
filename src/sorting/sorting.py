# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # Needs index counts for all three arrays(a, b, c)
    # Loop til indexes for both a and b are more than the length
    # of their respective list
    # index count for merged_arr will increment every time
    # other two will increment when value is smaller

    a = 0
    b = 0
    c = 0
    while a < len(arrA) and b < len(arrB):
        if arrA[a] < arrB[b]:
            merged_arr[c] = arrA[a]
            a += 1
            c += 1
        else:
            merged_arr[c] = arrB[b]
            c += 1
            b += 1
    while a < len(arrA):
        merged_arr[c] = arrA[a]
        a += 1
        c += 1
    while b < len(arrB):
        merged_arr[c] = arrB[b]
        c += 1
        b += 1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively


def merge_sort(arr):
    # Your code here
    # the array needs to be split down the middle
    # needs variables to hold left and right side indices
    # call merge sort on left and right side until theres one item
    # in each list (base case)
    # use the merge helper to merge all the split values
    if len(arr) > 1:
        middle = len(arr) // 2
        left_half = arr[:middle]
        right_half = arr[middle:]

        return merge(merge_sort(left_half), merge_sort(right_half))

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input


def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass
