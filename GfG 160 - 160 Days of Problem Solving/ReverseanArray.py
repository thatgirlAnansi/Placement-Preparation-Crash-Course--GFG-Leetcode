class Solution:
    def reverseArray(self, arr):
        # Two-pointer approach to reverse the array in-place
        left = 0
        right = len(arr) - 1
        
        while left < right:
            # Swap elements
            arr[left], arr[right] = arr[right], arr[left]
            # Move the pointers
            left += 1
            right -= 1 
