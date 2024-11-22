class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reachable = 0
        for i in range(len(nums)):
            if i > max_reachable:  # If we cannot reach this index
            return False
        max_reachable = max(max_reachable, i + nums[i])  # Update the farthest we can reach
        if max_reachable >= len(nums) - 1:  # If we can reach or exceed the last index
            return True
    return False  
