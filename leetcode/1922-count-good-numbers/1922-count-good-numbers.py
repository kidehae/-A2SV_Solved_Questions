class Solution:
    def countGoodNumbers(self, n: int) -> int:
        ods, evns = n // 2, ceil(n / 2)
        mod = 10 ** 9 + 7

        def mypow(x, n):
            if n == 1:
                return x
            if n == 0:
                return 1
            h = mypow(x, n // 2)
            if not n % 2:
                return h * h % mod
            return h * h * x % mod
        return mypow(5,evns) * mypow(4,ods)  % mod