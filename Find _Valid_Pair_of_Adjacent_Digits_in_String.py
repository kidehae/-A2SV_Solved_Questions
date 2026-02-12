class Solution:
    def findValidPair(self, s: str) -> str:
        s_counter = Counter(s)
        res = ""

        for i in s:
            val = s_counter[i]
            if val == int(i):
                if i in res:
                    continue
                res += i
                if len(res) == 2:
                    break
            else:
                res = ""

        if len(res) < 2:
            return ""
        else:
            return res

        
