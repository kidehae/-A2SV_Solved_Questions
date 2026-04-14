class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        prev = [[]]
        for n in nums:
            x = len(prev)
            for i in range (x):
                curr = prev[i] + [n]
                prev.append(curr)

        return prev
        