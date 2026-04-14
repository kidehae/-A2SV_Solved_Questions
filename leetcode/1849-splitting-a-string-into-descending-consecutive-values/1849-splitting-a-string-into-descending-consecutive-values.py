class Solution:
    def splitString(self, s: str) -> bool:

        arr = []

        def backtrack(val):

            if val >= len(s):
                for i in range(1,len(arr)):
                    if arr[i-1] - arr[i] != 1:
                        return False
                return len(arr) >= 2

            for i in range(val, len(s)):
                curr = int(s[val:i+1])
                arr.append(curr)
                if backtrack(i+1):
                    return True
                arr.pop()

            return False
        return backtrack(0)

