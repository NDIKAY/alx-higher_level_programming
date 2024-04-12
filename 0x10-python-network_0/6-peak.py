def find_peak(list_of_integers):
    """Find a peak element in a list of unsorted integers.
    
    Args:
        list_of_integers (list): The list of integers in which to find a peak.
        
    Returns:
        int: A peak element if found; otherwise, None.
    """
    def binary_search_peak(arr, low, high):
        """Helper function to perform binary search for finding a peak."""
        if low == high:
            return arr[low]
        
        mid = (low + high) // 2
        
        # Compare middle element with its neighbors
        if (mid == 0 or arr[mid] >= arr[mid - 1]) and (mid == len(arr) - 1 or arr[mid] >= arr[mid + 1]):
            return arr[mid]
        
        # If middle element is smaller than its left neighbor, search left half
        elif mid > 0 and arr[mid] < arr[mid - 1]:
            return binary_search_peak(arr, low, mid - 1)
        
        # If middle element is smaller than its right neighbor, search right half
        else:
            return binary_search_peak(arr, mid + 1, high)
    
    # Handle the case when the list is empty
    if not list_of_integers:
        return None
    
    # Perform binary search to find a peak
    return binary_search_peak(list_of_integers, 0, len(list_of_integers) - 1)
