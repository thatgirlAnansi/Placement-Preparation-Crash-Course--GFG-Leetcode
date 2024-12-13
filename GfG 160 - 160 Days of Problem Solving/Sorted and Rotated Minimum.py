
class Solution:
    def findMin(self, arr):
        #complete the function here        # Complete the function here
        low, high = 0, len(arr) - 1

        # If the array is not rotated at all
        if arr[low] <= arr[high]:
            return arr[low]

        while low <= high:
            mid = (low + high) // 2

            # Check if mid is the minimum element
            if mid > 0 and arr[mid] < arr[mid - 1]:
                return arr[mid]

            # Check if mid+1 is the minimum element
            if mid < len(arr) - 1 and arr[mid] > arr[mid + 1]:
                return arr[mid + 1]

            # Decide which half to go
            if arr[mid] >= arr[low]:
                low = mid + 1
            else:
                high = mid - 1

        return -1  # This line is theoretically unreachable
