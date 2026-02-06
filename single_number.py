class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        nums_counter = Counter(nums)
        ans = 0
        for key, val in nums_counter.items():
            
            if val ==  1:
                ans = key
                break

        return ans

