class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        min_prefix = float("inf")
        summ = 0
        for i in nums:
            summ += i
            min_prefix = min(min_prefix, summ)

        

        return max(1, 1 - min_prefix)


