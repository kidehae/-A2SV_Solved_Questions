class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        counter = Counter()
        r = 0
        l = 0
        max_width = 0
        max_freq = 0

        while r < len(nums):
            counter[nums[r]] += 1
            while counter[0] > 1:
                counter[nums[l]] -= 1
                l += 1
                

            max_width = max(max_width, r - l)
            r += 1

        return max_width


