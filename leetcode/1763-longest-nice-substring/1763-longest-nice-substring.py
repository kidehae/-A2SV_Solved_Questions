class Solution:
    def longestNiceSubstring(self, s: str) -> str:

        if len(s) < 2:
            return  ""
        
        sett = set(s)
        for i, val in enumerate(s):
            if val.swapcase() not in sett:
                left = self.longestNiceSubstring(s[:i])
                right = self.longestNiceSubstring(s[i + 1:])
                if len(left) >= len(right):
                    return left
                else:
                    return right

        return s

            
        
        