class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        v = len(nums) // 3
        nums_counter = Counter(nums)
        res = []

        for key, val in nums_counter.items():
            if val > v:
                res.append(key)

        return res

        
