class Solution:
    def isPowerOfFour(self, n: int) :

        if n <= 0:
            return False
        def poweroffour(x)-> bool:
            if x == 1:
                return True
            if x % 4 != 0:
                return False
            return poweroffour(x // 4)
            
        return(poweroffour(n))



        