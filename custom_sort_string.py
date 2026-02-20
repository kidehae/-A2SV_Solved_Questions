class Solution:
    def customSortString(self, order: str, s: str) -> str:
        s = list(s)
        s_counter = Counter(s)
        new_str = ""
        for i in order:
            if s_counter[i] > 0:
                new_str += i * s_counter[i]
                del s_counter[i]

        for key, val in s_counter.items():
            if key not in new_str:
                new_str += key * val

        
        return new_str
            

        
