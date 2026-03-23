class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        def pow3(x):
            if x == 1:
                return True
            if x < 3:
                return False
           
            x = x / 3
            return pow3(x)
            
        return pow3(n)
        
        