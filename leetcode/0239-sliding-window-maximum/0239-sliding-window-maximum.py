class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        queue = deque()
        for i, val in enumerate(nums):
            while queue and nums[queue[-1]] <= val:
                queue.pop()
            if queue and  i - queue[0] >= k:
                queue.popleft()

            queue.append(i)
            res.append(nums[queue[0]])

        return res[k-1:]
            


       