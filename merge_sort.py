# Name: Weevern Gong
# Project Title: MSCS532_Assignment2
# Description: This program implements the merge sort algorithm to sort a list of integers in monotonically increasing order.
# Merge sort divides the list into smaller portions, sorts those portions recursively, and then merges them back together.

# Merge sort explanation: The merge sort algorithm works by repeatedly dividing the list into two smaller portions.
# The division continues until each portion contains only one element, which is already considered sorted. The algorithm then
# combines the smaller sorted portions by comparing their values and placing them into the correct order.
# During the merge step, the smaller current value from the two portions is copied into temporary storage. Any remaining values
# are then copied after it, and the merged result is copied back into the original list.
# The input is a list of integers, and the output is the same list sorted in increasing order.
# The algorithm uses temporary storage during the merge process.
# Its best-case, average-case, and worst-case time complexities are all Θ(n log n), where n is the number of elements in the input list.


def merge_sort(arr):

    # If the list has zero or one element, it is already sorted
    if len(arr) <= 1:
        return arr

    # Create temporary storage that will be reused during the merge process
    temp_arr = [0] * len(arr)

    # Sort the entire list from the first index to the last index
    merge_sort_recursive(arr, temp_arr, 0, len(arr) - 1)

    return arr


def merge_sort_recursive(arr, temp_arr, left, right):

    # Continue dividing while the current portion contains more than one element
    if left < right:

        # Find the middle index to divide the current portion into two halves
        middle = (left + right) // 2

        # Recursively sort the left half
        merge_sort_recursive(arr, temp_arr, left, middle)

        # Recursively sort the right half
        merge_sort_recursive(arr, temp_arr, middle + 1, right)

        # Merge the two sorted halves back together
        merge(arr, temp_arr, left, middle, right)


def merge(arr, temp_arr, left, middle, right):

    i = left
    j = middle + 1
    k = left

    # Compare values from both halves and copy the smaller value into temporary storage
    while i <= middle and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            i += 1
        else:
            temp_arr[k] = arr[j]
            j += 1
        k += 1

    # Copy any values remaining in the left half
    while i <= middle:
        temp_arr[k] = arr[i]
        i += 1
        k += 1

    # Copy any values remaining in the right half
    while j <= right:
        temp_arr[k] = arr[j]
        j += 1
        k += 1

    # Copy the merged values back into the original list
    for i in range(left, right + 1):
        arr[i] = temp_arr[i]


def main():

    numbers_arr = [5, 2, 20, 9, 1, 5, 6, 3, 71, 8, 4, 56, 12]

    print("Input array:", numbers_arr)

    sorted_arr = merge_sort(numbers_arr)

    print("Array sorted in monotonically increasing order using Merge Sort:", sorted_arr)


if __name__ == "__main__":
    main()
