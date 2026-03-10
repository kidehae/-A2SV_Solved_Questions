class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stck = []
        res = [0]  * len(temperatures) 

        for idx, val in enumerate(temperatures):
            while stck and stck[-1][0] < val:
                v, i = stck.pop()
                res[i] = idx - i
            stck.append([val,idx])

        return res
                