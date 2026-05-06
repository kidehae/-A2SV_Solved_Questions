# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        val = root.val

        def bfs(root):
            if not root:
                return True

            if root.val != val:
                return False

            left = bfs(root.left)
            right = bfs(root.right)

            return left and right

        return bfs(root)



        