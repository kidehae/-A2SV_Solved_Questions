class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stck = []
        res = 0
        for i in s:
            nested = False
            if i == "(":
                stck.append(i)
            else:
                summ = 0
                while stck and  stck[-1] != "(":
                    summ += stck.pop()
                    nested = True
                stck.pop()

                if nested:
                    stck.append(summ * 2)
                else:
                    stck.append(1)

        return sum(stck)

        