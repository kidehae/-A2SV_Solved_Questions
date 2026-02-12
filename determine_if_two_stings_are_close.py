class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        word1_count = dict(sorted(Counter(word1).items(), key = lambda x: (x[1])))
        word2_count = dict(sorted(Counter(word2).items(), key = lambda x: (x[1])))

        if set(word1_count.keys()) != set(word2_count.keys()):
            return False

        list1 = list(word1_count.values())
        list2 = list(word2_count.values())

        return list1 == list2


        
