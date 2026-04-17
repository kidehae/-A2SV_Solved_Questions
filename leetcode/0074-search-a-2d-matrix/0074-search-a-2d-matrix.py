class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def bs(arr):
            l = 0
            r = len(arr) - 1
            while l <= r:
                m = (l+r) // 2
                if arr[m] == target:
                    return True
                if arr[m] > target:
                    r = m - 1
                if arr[m] < target:
                    l = m + 1
            return False

        for arr in  matrix:
            if arr[0] <= target and bs(arr):
                return True
            elif arr[0] > target:
                return False

        return False

         