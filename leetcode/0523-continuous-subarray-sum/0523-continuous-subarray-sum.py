class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        count = { 0: -1}
        summ = 0
        for i in range(len(nums)):
            summ += nums[i]
            r = summ % k
            if r not in count:
                count[r] = i
            elif i - count[r] > 1:
                return True

        return False

            




        
        