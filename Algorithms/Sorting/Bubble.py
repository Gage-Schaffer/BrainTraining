"""
One of the simplest sorting algorithms that works by repeatedly swapping the adjacent elements if they are in the
wrong order. Not suitable for very large datasets.

https://www.geeksforgeeks.org/bubble-sort/

Time complexity: O(n^2), Omega(n) if the list is already sorted
"""

unsorted_arr = [9, 5, 3, 4, 1, 2, 6, 7, 8]


def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break


bubble_sort(unsorted_arr)
print(unsorted_arr)
