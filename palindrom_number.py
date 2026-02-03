class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
       
        x = str(x)
        x = list(x)
        newx = []
        for i in x[::-1]:
            newx.append(i)
        
        
        if x == newx:
            return True
        else:
            return False
       
        
