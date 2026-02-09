class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_count = Counter(nums)
        sorted_nums = dict(sorted(nums_count.items(), key = lambda x: x[1], reverse = True ))
        print(sorted_nums)
        res = []
        j  = 0
        for key, val in sorted_nums.items():
            if j < k:
                res.append(key)
                j += 1
            else:
                break
            
        
        return res


        
