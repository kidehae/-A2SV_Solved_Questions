class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:


        def combine(num, path):
            if len(path) == k:
                res.append(path[:])
                return

            for i in range (num, n + 1):
                path.append(i)
                combine(i + 1, path)
                path.pop()

        res = []
        combine(1,[])
        return res


        