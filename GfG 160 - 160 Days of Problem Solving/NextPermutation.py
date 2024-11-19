class Solution:
    def nextPermutation(self, arr):
        """
        :type nums: List[int]
        :rtype: None (modifies nums in-place)
        """
        n = len(arr)
        i = n - 2
        
        # Step 1: Find the first decreasing element
        while i >= 0 and arr[i] >= arr[i + 1]:
            i -= 1
        
        if i >= 0:  # Step 2: Find the next larger element
            j = n - 1
            while arr[j] <= arr[i]:
                j -= 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap
        
        # Step 3: Reverse the array from i+1 to end
        arr[i + 1:] = reversed(nums[i + 1:])
