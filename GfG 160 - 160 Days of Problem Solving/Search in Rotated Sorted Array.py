class Solution:
    def search(self, arr, key):
        # Define the search boundaries
        low, high = 0, len(arr) - 1

        while low <= high:
            mid = (low + high) // 2

            # Check if mid is the key
            if arr[mid] == key:
                return mid

            # Check which half is sorted
            if arr[low] <= arr[mid]:  # Left half is sorted
                if arr[low] <= key < arr[mid]:
                    high = mid - 1  # Key is in the left half
                else:
                    low = mid + 1   # Key is in the right half
            else:  # Right half is sorted
                if arr[mid] < key <= arr[high]:
                    low = mid + 1   # Key is in the right half
                else:
                    high = mid - 1  # Key is in the left half

        # Key not found
        return -1
