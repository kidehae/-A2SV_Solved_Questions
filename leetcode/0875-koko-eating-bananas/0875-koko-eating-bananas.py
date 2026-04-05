class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def check(k):
            hr = 0
            for i in piles:
                hr += ceil(i/k)
                if hr > h:
                    return False
            return True 

        low = 1
        high = max(piles)

        while low <= high:
            m = (low + high) // 2

            if check(m):
                high = m - 1
            else:
                low = m + 1

        return low


        