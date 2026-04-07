class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        nums = nums1 + nums2
        n = len(nums)
        nums.sort()
        if n % 2:
            return float(nums[n // 2])
        else:
            n = n // 2
            return ((nums[n] + nums[n-1]) / 2)

        