class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        nums2 = sorted(nums)
        result = []
        for i in nums:
            result.append(nums2.index(i))
        return result

        
