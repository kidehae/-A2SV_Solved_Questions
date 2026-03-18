# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        

        if root == None:
            return []
        stck = [root]
        res = []

        while stck:
            node = stck.pop()
            res.append(node.val)

            if node.right:
                stck.append(node.right)
            if node.left:
                stck.append(node.left)

        return res


        