# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:


        def isgreater(root, mx):
            if not root:
                return True
            if root.val <= mx:
                return False

            return isgreater(root.left, mx) and isgreater(root.right, mx)


        def issmaller(root, mn):
            if not root:
                return True
            if root.val >= mn:
                return False

            return issmaller(root.left, mn) and issmaller(root.right, mn)


        if not root:
            return True

        if root.left and root.val <= root.left.val:
            return False

        if root.right and root.val >= root.right.val:
            return False

        if not isgreater(root.right, root.val):
            return False

        if not issmaller(root.left, root.val):
            return False
        
        return self.isValidBST(root.right) and self.isValidBST(root.left)


        

        

        

        
        