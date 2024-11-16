class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None (modifies nums in-place)
        """
        n = len(nums)
        i = n - 2
        
        # Step 1: Find the first decreasing element
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        if i >= 0:  # Step 2: Find the next larger element
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]  # Swap
        
        # Step 3: Reverse the array from i+1 to end
        nums[i + 1:] = reversed(nums[i + 1:])
