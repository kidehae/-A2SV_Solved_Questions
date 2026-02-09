class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        arr = []
        for i in range(0,len(nums)):
            
            n = target-nums[i]
            
            if (n in nums):
                ind = nums.index(n)

            if (n in nums) and (ind != i):
                arr.append(i)
                arr.append(ind)
                break


        return arr
