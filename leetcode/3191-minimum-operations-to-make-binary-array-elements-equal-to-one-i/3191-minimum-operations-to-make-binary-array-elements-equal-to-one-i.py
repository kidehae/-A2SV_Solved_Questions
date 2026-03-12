class Solution:
    def minOperations(self, nums: List[int]) -> int:

        nums = deque(nums)
        count = 0

        for i in range(len(nums)):
            if nums[0] == 1:
                nums.popleft()
                continue

            if len(nums) < 3:
                return -1

            for j in range(3):
                nums[j] = 1 - nums[j]

            count += 1
            nums.popleft()
        
        return count
            
           
            
        