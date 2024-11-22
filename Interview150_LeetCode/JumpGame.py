from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reachable = 0  # Initialize the farthest index we can reach
        for i in range(len(nums)):
            if i > max_reachable:  # If the current index is beyond our reach
                return False
            max_reachable = max(max_reachable, i + nums[i])  # Update the farthest reachable index
        return max_reachable >= len(nums) - 1  # Check if we can reach or exceed the last index
