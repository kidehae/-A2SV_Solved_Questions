from collections import Counter

class Solution:
    def checkEqual(self, a, b) -> bool:
        
       acount = Counter(a)
       bcount = Counter(b)
       
       for i in a:
           if acount[i] != bcount[i]:
               
               return False
           
       return True
                
        
           
            
        #code here
