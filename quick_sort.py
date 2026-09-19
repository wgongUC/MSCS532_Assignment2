# Name: Weevern Gong
# Project Title: MSCS532_Assignment2
# Description: This program implements the quick sort algorithm to sort a list of integers in monotonically increasing order.
# The last value in each portion of the list is selected as the pivot for the partitioning process.

# Quick sort explanation: The quick sort algorithm works by selecting a pivot and dividing the list around that pivot.
# In this implementation, the last value in the current portion is used as the pivot. Values that are less than or equal to
# the pivot are moved to its left, while larger values remain on its right. The pivot is then moved into its final sorted position.
# The algorithm recursively repeats this process on the portions to the left and right of the pivot until the entire list is sorted.
# The input is a list of integers, and the output is the same list sorted in increasing order.
# The algorithm sorts the list in place, so another list does not need to be created for the partitioning process.
# Its best-case and expected average-case time complexities are Θ(n log n). Its worst-case time complexity is Θ(n^2) when the partitions
# are repeatedly unbalanced, which can occur with sorted or reverse-sorted input when the last value is always selected as the pivot.


def quick_sort(arr):

    # Sort the entire list from the first index to the last index
    quick_sort_recursive(arr, 0, len(arr) - 1)

    return arr


def quick_sort_recursive(arr, low, high):

    # Continue partitioning while the current portion contains more than one element
    if low < high:

        # Partition the current portion and place the pivot into its final sorted position
        pivot_index = partition(arr, low, high)

        # Recursively sort the values to the left of the pivot
        quick_sort_recursive(arr, low, pivot_index - 1)

        # Recursively sort the values to the right of the pivot
        quick_sort_recursive(arr, pivot_index + 1, high)


def partition(arr, low, high):

    # Use the last value in the current portion as the pivot
    pivot = arr[high]
    i = low - 1

    # Move values less than or equal to the pivot toward the left side
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # Move the pivot after the values that are less than or equal to it
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


def main():

    numbers_arr = [5, 2, 20, 9, 1, 5, 6, 3, 71, 8, 4, 56, 12]

    print("Input array:", numbers_arr)

    sorted_arr = quick_sort(numbers_arr)

    print("Array sorted in monotonically increasing order using Quick Sort:", sorted_arr)


if __name__ == "__main__":
    main()
