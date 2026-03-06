class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sub_arr = nums[0]
        current = 0

        for i in nums:
            if current < 0:
                current = 0
            current += i
            max_sub_arr = max(max_sub_arr, current)

        return max_sub_arr
        
