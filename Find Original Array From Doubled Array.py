class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:

        if len(changed) % 2 != 0:
            return [] 
        changed.sort()
        c_count = Counter(changed)
        orginal = []

        for i in changed:

            if c_count [i] == 0:
                continue
            c_count[i] -= 1
            

            j = i*2
            c_count[j] = c_count.get(j, 0)

            if  c_count[j] > 0:
                orginal.append(i)
                c_count[j] -= 1

            else:
                return []


        return orginal
           

        
        
