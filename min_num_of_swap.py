class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        table = defaultdict(int)
        for a, b in zip(s1, s2):
            table[a + b] += 1
        xy = table["xy"]
        yx = table["yx"]

        if (xy + yx) % 2 == 1:
            return -1
        return (xy // 2) + (yx // 2) + xy % 2 + yx % 2  




