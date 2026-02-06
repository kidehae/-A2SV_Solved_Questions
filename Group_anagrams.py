class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams = defaultdict(list)

        for i in strs:
            j = i
            i = "".join(sorted(i))
            anagrams[i].append(j)
        
        res = []
        for key, val in anagrams.items():
            res.append(val)

        return res
        

        
