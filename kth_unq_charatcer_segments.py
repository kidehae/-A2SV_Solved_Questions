class Solution:
    def subarraysWithKDistinct(self, nums, k):

        def atMost(k):
            freq = defaultdict(int)
            l = 0
            res = 0

            for r in range(len(nums)):
                freq[nums[r]] += 1

                while len(freq) > k:
                    freq[nums[l]] -= 1
                    if freq[nums[l]] == 0:
                        del freq[nums[l]]
                    l += 1
                res += r - l + 1
            return res
        return atMost(k) - atMost(k-1)
