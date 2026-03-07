class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        def counter(x):
            l, summ = 0, 0
            res = 0
            for r in range(len(nums)):
                summ += nums[r]
                while summ > x and l <= r:
                    summ -= nums[l]
                    l += 1
                res += (r - l) + 1
            return res
        return (counter(goal) - counter(goal - 1))
                



        
