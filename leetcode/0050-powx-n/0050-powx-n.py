class Solution:

    @cache
    def myPow(self, x: float, n: int) -> float:

        if n == 0:
            return 1
        if n == 1:
            return x

        if n == -1:
            return 1 / x
        
        c = n / 2

        return self.myPow(x,ceil(c)) * self.myPow(x,floor(c))
         

    

