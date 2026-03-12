class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stck = []
        mn = nums[0]
        for i in nums:
            while stck and i >= stck[-1][0]:
                stck.pop()
            if stck and i > stck[-1][1]:
                return True
            stck.append([i, mn])
            mn = min(mn, i)

        return False



        