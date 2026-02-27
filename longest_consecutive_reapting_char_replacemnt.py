class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = Counter()
        max_char = 0
        r = 0
        l = 0
        max_width = 0

        while r < len(s):
            counter[s[r]] += 1
            max_char = max( max_char, counter[s[r]])
            w = r - l + 1
            while k < (w - max_char):
                counter[s[l]] -= 1
                l += 1
                w = r - l + 1

            max_width = max(max_width,w)
            r += 1

        return max_width

            

            


        
