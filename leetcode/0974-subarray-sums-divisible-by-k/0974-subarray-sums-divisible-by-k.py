class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        res = 0
        summ = 0
        count = { 0:1 }
        for i in nums:
            summ += i
            r = summ % k

            if r in count:
                res += count[r]

            count[r] = count.get(r, 0) + 1
        
        return res
        