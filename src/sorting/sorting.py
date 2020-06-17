# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # Needs counts for arrA and arrB
    # For loop holds merged_arr count
    # Loop til counts for both a and b are equal to the length
    # of their respective list
    # count for merged_arr will increment  w/ for loop
    # other two will increment when value is smaller

    a = 0
    b = 0
    for c in range(elements):
        if a == len(arrA):
            merged_arr[c] = arrB[b]
            b += 1
        elif b == len(arrB):
            merged_arr[c] = arrA[a]
            a += 1
        elif arrA[a] < arrB[b]:
            merged_arr[c] = arrA[a]
            a += 1
        else:
            merged_arr[c] = arrB[b]
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
    start2 = mid + 1

    # If the direct merge is already sorted
    if (arr[mid] <= arr[start2]):
        return

    # Two pointers to maintain start
    # of both arrays to merge
    while (start <= mid and start2 <= end):

        # If element 1 is in right place
        if (arr[start] <= arr[start2]):
            start += 1
        else:
            value = arr[start2]
            index = start2

            # Shift all the elements between element 1
            # element 2, right by 1.
            while (index != start):
                arr[index] = arr[index - 1]
                index -= 1

            arr[start] = value

            # Update all the pointers
            start += 1
            mid += 1
            start2 += 1


def merge_sort_in_place(arr, l, r):
    if (l < r):

        # Same as (l + r) / 2, but avoids overflow
        # for large l and r
        m = l + (r - l) // 2

        # Sort first and second halves
        merge_sort_in_place(arr, l, m)
        merge_sort_in_place(arr, m + 1, r)

        merge_in_place(arr, l, m, r)
