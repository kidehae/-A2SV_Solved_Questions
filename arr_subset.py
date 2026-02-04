from collections import Counter
class Solution:
    
    def isSubset(self, a, b):
        
       acount = Counter(a)
       bcount = Counter(b)
       
       for i in b:
           if acount[i] < bcount[i]:
               
               return False
           
       return True
        
        

    
    
