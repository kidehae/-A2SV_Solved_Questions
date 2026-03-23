# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def check(r,s):
            if r == s == None:
                return True
            if not r or not s or s.val != r.val:
                return False

            return (check(r.left,s.left) and (check(r.right,s.right)))

        if not root:
            return False
        if check(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

        