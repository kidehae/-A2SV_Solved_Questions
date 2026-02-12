class Solution:
    def frequencySort(self, s: str) -> str:
        f = Counter(s)
        StrList = list(s)
        StrList.sort(key = lambda x: (-f[x], x))
        
        return  "".join(StrList)
