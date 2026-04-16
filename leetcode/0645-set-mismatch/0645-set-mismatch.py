class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        f = Counter(nums)
        x = -1
        y = -1

        for i in range (1, n+1):
            if f[i] == 2:
                x = i
            elif f[i] == 0:
                y = i
        return [x,y]

           

        
