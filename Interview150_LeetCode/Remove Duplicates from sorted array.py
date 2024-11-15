class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        
        temp = [0] * len(nums)
        temp[0] = nums[0]
        res = 1

        for i in range(1, len(nums)):
            if temp[res - 1] != nums[i]:
                temp[res] = nums[i]
                res += 1

        for i in range(res):
            nums[i] = temp[i]

        return res
