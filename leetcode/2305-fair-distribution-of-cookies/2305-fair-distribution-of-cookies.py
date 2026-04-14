class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        basket = [0] * k
        self.res = float("inf")

        def backtrack(i, basket):

            if i >= len(cookies):
                self.res = min (self.res, max(basket))
                return

            if max(basket) > self.res:
                return

            for j in range(k):
                basket[j] += cookies[i]
                backtrack(i+1, basket)
                basket[j] -= cookies[i]

        backtrack(0, basket)
        return self.res


