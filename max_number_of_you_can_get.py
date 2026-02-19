class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        nums = piles
        nums.sort()
        num_of_pairs = len(nums)//3
        summ = 0
        for i in range(num_of_pairs, len(nums),2):
            summ += nums[i]
        return summ


        
