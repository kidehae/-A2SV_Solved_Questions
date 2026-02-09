class Solution:
    def sumOfThree(self, num: int) -> List[int]:
         res = []
         
         n = num // 3

         if n-1 + n+1 + n == num:
            res.append(n-1)
            res.append(n)
            res.append(n+1)

         return res



        
