class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def check(k):
            summ = 0
            day = 1

            for i in weights:
                summ += i
                if summ > k:
                    day += 1
                    summ = i
                if day > days:
                    return False

            return True

        l = max(weights)
        h = sum(weights)

        while l <= h:
            m = (l + h) // 2

            if check(m):
                h = m - 1
            else:
                l = m + 1

        return l
        
             
        