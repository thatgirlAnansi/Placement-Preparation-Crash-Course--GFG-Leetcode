class Solution {
    public int majorityElement(int[] nums) {
        int res = 0;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] > nums[res]) {
                res = i;
            }
        }
        return nums[res];
    }
}
