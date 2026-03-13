class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        cashes = { 20:0, 10:0, 5:0 }

        for i in bills:
            j = i
            i -= 5

            for k,v in cashes.items():
                c = min((i // k) , v)
                i -= (c * k)
                cashes[k] -= c

            if i > 0 :
                return False
            cashes[j] += 1

        return True
            


       

        