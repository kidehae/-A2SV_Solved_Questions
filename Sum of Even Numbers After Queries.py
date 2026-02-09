class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]

        res = []
        even_sum = 0

        for num in nums:
            if num % 2 == 0:
                even_sum += num

        for q in queries:
            org = nums[q[1]]
            new_org = org + q[0]
            nums[q[1]] = new_org

            if org % 2 == 0:
                even_sum -= org
            if new_org % 2 == 0:
                even_sum += new_org

            res.append(even_sum)

        return res

        


        
