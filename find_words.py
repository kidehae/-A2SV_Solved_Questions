class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        c_chars = Counter(chars)
        tot = 0

        for word in words:
            good = True
            c_word = Counter(word)
            for j in word:
                if j in chars:
                   if c_word[j] > c_chars[j]:
                    good = False
                    break

                else:
                    good = False
            
            if good:
                tot += len(word)

        return tot






    
        
