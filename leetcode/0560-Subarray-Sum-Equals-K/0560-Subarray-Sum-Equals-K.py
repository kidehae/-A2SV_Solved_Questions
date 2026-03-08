class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        count = { 0:1 }
        res = 0
        summ = 0
        for i in nums:
            summ += i
            dif = summ - k
            if dif in count:
                res += count[dif]
            
            count[summ] = count.get(summ, 0) + 1

        return res