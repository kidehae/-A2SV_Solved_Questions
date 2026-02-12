class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(set(nums))
        count = 1
        prev = 0

        if not nums:
            return prev

        for i in range (len(nums)):
            if i < len(nums)-1 and  nums[i+1] == nums[i] + 1:
                count = count + 1
            else:
                prev = max(prev, count)
                count = 1
        return max(prev, count)

        
