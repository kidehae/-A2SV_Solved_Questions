# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def diver(l, r):
            if l > r:
                return None
            m = (r + l) // 2
            l = diver(l, m - 1)
            r = diver(m+1, r)
            return TreeNode(nums[m], l, r)

        return diver(0, len(nums) - 1)




            
        