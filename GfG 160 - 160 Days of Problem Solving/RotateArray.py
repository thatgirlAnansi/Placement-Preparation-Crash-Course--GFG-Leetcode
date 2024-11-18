class Solution:
    # Function to rotate array in place by d elements
    def rotateArr(self, arr, d):
        n = len(arr)
        d = d % n  # Normalize d to handle cases where d > n
        
        # Reverse the first part (0 to d-1)
        self.reverse(arr, 0, d - 1)
        
        # Reverse the second part (d to n-1)
        self.reverse(arr, d, n - 1)
        
        # Reverse the entire array
        self.reverse(arr, 0, n - 1)
    
    # Helper function to reverse a subarray from index 'start' to 'end'
    def reverse(self, arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
