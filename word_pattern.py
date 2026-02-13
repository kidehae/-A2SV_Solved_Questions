class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        ppattern = list(map(pattern.index, pattern))
        words = s.split()
        spattern = list(map(words.index, words))

        if ppattern == spattern:
            return True
        else:
            return False

        
