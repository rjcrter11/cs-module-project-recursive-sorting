# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # list needs to be split down the middle
    # between 0 and last index
    # if target is the middle, return that index
    # if its bigger, call binary search on itself (w/ last index - 1)
    # if its smaller, call binary search on itself (w/ 0 index + 1)
    if end >= start:
        middle = (end + start) // 2
        if arr[middle] == target:
            return middle
        elif arr[middle] > target:
            end = middle - 1
            return binary_search(arr, target, start, end)
        else:
            start = middle + 1
            return binary_search(arr, target, start, end)
    else:
        return -1

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively
# or iteratively


def agnostic_binary_search(arr, target):
    # Your code here
    pass
