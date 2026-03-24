# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:

        summ = 0

        if not root:
            return 0

        if root and (root.left or root.right) and root.val % 2 == 0:
            if root.left and root.left.left:
                summ += root.left.left.val

            if root.left and root.left.right:
                summ += root.left.right.val

            if root.right and root.right.left:
                summ += root.right.left.val
            
            if root.right and root.right.right:
                summ += root.right.right.val

        return summ + self.sumEvenGrandparent(root.left) + self.sumEvenGrandparent(root.right)
        