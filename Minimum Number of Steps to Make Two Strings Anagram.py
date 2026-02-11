class Solution:
    def minSteps(self, s: str, t: str) -> int:
        k = 0
        s_count = Counter(s)
        t_count = Counter(t)
        for i in s_count:
            t_count[i] = t_count.get(i,0)
            if t_count[i] < s_count[i]:
                dif = s_count[i] - t_count[i]
                k += dif
                t_count[i] -= dif

        return k


            
        

        return k
        
