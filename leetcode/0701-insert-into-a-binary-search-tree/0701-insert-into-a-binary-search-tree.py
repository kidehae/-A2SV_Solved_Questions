# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        new_node = TreeNode(val)

        def iterate(root):

            if root == None:
                return new_node

            if val > root.val:
                root.right = iterate(root.right)
                return root
            else:
                root.left = iterate(root.left)
                return root
        return iterate(root)

        