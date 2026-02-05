class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        nums_count = Counter(nums)
        res = []
        for key, val in nums_count.items():
            if nums_count[key] == 2:
                res.append(key)

        return res
        
