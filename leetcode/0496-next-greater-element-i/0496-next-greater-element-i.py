class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stck = []
        mapp = {}

        for i in reversed(nums2):
            while stck and stck[-1] <= i:
                stck.pop()
            if not stck:
                mapp[i] = -1
            else:
                mapp[i] = stck[-1]
            stck.append(i)

        res = []
        for i in nums1:
            res.append(mapp[i])

        return res

        