class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        allSet = set()
        for i in nums :
            if i in allSet:
                return True
            else:
                allSet.add(i)
        return False
                                  
