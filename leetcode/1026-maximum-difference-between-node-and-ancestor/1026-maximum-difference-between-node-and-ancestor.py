# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        def find(root, mn, mx):

            if not root:
                return mx - mn

            mx = max (root.val, mx)
            mn = min (root.val, mn)

            leftmax = find(root.left, mn, mx)
            rightmax = find(root.right, mn, mx)

            return max(leftmax, rightmax)

        return find(root, root.val, root.val)
            

        
        