class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        mxarea = 0
        stck = []
        for i, h in enumerate(heights):
            s = i
            while stck and stck[-1][1] > h:
                idx, hi = stck.pop()
                A = hi * (i - idx)
                mxarea = max(A,mxarea)
                s = idx
            stck.append([s, h])

        for i,h in stck:
            mxarea = max(mxarea, h * (len(heights) - i))

        return mxarea


        