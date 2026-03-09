class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        dif_arr = [0] * (len(nums) + 1)

        for l, r in requests:
            dif_arr[l] += 1
            dif_arr[r + 1] -= 1   

        arr = [0] * len(nums)
        val = 0
        for i in range(len(nums)):
            val += dif_arr[i]
            arr[i] = val

        nums.sort()
        arr.sort()

        MOD = 10**9 + 7
        res = 0

        for i, j in zip(arr, nums):
            res = (res + i * j) % MOD

        return res