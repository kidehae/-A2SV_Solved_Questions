class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        miss = 1
        i = 0
        p = 0

        while miss <= n:
            if i < len(nums) and miss >= nums[i]:
                miss += nums[i]
                i += 1
            else:
                miss += miss
                p += 1

        return p
