class Solution:
    def numRabbits(self, answers: List[int]) -> int:

        c = Counter(answers)
        res = 0

        for k, v in c.items():
            k += 1
            x = ceil(v / k) * k
            res += x

        return res



        