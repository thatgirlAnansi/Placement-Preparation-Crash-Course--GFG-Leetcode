class Solution:   
    def peakElement(self,arr):
        n = len(arr)
        low, high = 0, n - 1
        
        while low <= high:
            mid = (low + high) // 2
            
            # Check if mid is a peak element
            left = float('-inf') if mid == 0 else arr[mid - 1]
            right = float('-inf') if mid == n - 1 else arr[mid + 1]
            
            if arr[mid] > left and arr[mid] > right:
                return mid
            
            # Move to the side of the larger neighbor
            if arr[mid] < right:
                low = mid + 1
            else:
                high = mid - 1
    
        return -1  # Should not happen given valid input
