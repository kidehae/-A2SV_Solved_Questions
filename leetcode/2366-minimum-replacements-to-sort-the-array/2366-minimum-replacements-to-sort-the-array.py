class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        r_bound = nums[-1]
        op = 0
        for i in nums[::-1]:
            n = (i + r_bound - 1 )// r_bound
            op += n - 1
            r_bound  = i // n

        return op
        