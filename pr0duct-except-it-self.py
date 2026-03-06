class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        before = []
        after = []
        p = 1

        for i in nums:
            before.append(p)
            p *= i

        p = 1

        for i in nums[::-1]:
            after.append(p)
            p *= i

        res = []

        for i,j in zip(before, after[::-1]):
            res.append( i * j)

        return res

        



        
