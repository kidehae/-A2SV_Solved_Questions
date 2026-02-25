class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        left = 0
        right = 1
        checker = 0
        counter = Counter(s)
        res = []

        while checker < len(s):

            current = s[left:right]

            if counter[s[checker]] == current.count(s[checker]):
                if checker - left + 1 == len(current) :
                    print(checker - left + 1)
                    print(len(current))
                    res.append(len(current))
                    left = checker + 1
                checker += 1
                
            elif right <= len(s):
                right += 1

        return res






            
                



        
