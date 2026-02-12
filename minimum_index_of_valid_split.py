class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        nums_counter = sorted(Counter(nums).items(), key=lambda x: x[1])
        dom_num, dom_freq = nums_counter[-1]
        
        count = 0
        
        for i in range(len(nums)):
            if nums[i] == dom_num:
                count += 1
            if (i+1) // 2 < count:
                left = dom_freq - count
                if left > (len(nums) - i - 1)//2:
                    return i
                else:
                    return -1

    
    

        

        
        
        
        
