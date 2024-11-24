class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr):
        
        max_so_far = float('-inf')  # Stores the maximum sum found so far
        max_ending_here = 0  # Stores the sum of the current subarray
        
        for num in arr:
            # Update the current subarray sum
            max_ending_here = max(num, max_ending_here + num)
            # Update the global maximum sum if needed
            max_so_far = max(max_so_far, max_ending_here)
        
        return max_so_far
