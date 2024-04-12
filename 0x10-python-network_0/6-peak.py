#!/usr/bin/python3

def find_peak(list_of_integers):
    """Finds a peak element in a list of unsorted integers.

    A peak element is an element that is greater than or equal to its neighbors.
    The function uses a binary search approach to find a peak in the list with
    O(log(n)) complexity.

    Args:
        list_of_integers (list): The list of integers to search.

    Returns:
        int or None: A peak element if found, otherwise None.
    """
    def binary_search_peak(arr, low, high):
        """Binary search to find a peak element in the list.

        Args:
            arr (list): The list of integers to search.
            low (int): The lower bound index for the search.
            high (int): The upper bound index for the search.

        Returns:
            int: A peak element if found, otherwise None.
        """
        if low == high:
            return arr[low]

        mid = (low + high) // 2

        # Check if the middle element is a peak
        if (mid == 0 or arr[mid] >= arr[mid - 1]) and (mid == len(arr) - 1 or arr[mid] >= arr[mid + 1]):
            return arr[mid]

        # Recurse into the left half if the middle element is smaller than its left neighbor
        elif mid > 0 and arr[mid] < arr[mid - 1]:
            return binary_search_peak(arr, low, mid - 1)

        # Recurse into the right half if the middle element is smaller than its right neighbor
        else:
            return binary_search_peak(arr, mid + 1, high)

    # Handle empty list case
    if not list_of_integers:
        return None

    # Find peak element using binary search
    return binary_search_peak(list_of_integers, 0, len(list_of_integers) - 1)

