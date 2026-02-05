class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        k = float("inf")
        commons = []

        for i in list1:
            if i in list2:
                s = list1.index(i) + list2.index(i)
                if s < k:
                    k = s
                    commons = []
                    commons.append(i)
                elif s == k:
                    commons.append(i)


        return commons
