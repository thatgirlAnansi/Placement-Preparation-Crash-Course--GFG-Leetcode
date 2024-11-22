class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n  # Handle cases where k > n
        
        # Reverse the entire array
        nums.reverse()
        # Reverse the first k elements
        nums[:k] = reversed(nums[:k])
        # Reverse the remaining elements
        nums[k:] = reversed(nums[k:])
