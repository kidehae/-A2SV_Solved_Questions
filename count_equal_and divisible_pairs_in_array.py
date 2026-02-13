class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        count = 0
        n = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j] and i*j % k == 0 and [i,j] not in n:
                    count += 1
                    nums.append([i,j])
        return count


