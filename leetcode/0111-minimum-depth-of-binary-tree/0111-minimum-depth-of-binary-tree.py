# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        def min_depth(root):
            if not root:
                return 0
            if not root.left and not root.right:
                return 1

            left = float('inf')
            right = float('inf')

            if root.left:
                left =  1 + min_depth(root.left)
            if root.right:
                right = 1 + min_depth(root.right)

            return  min(left, right)

        return min_depth(root)

        