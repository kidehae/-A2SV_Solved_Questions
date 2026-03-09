class Solution:
    def removeStars(self, s: str) -> str:
        stck = []
        for i in s:
            if stck and i == "*":
                stck.pop()
            else:
                stck.append(i)

        return "".join(stck)