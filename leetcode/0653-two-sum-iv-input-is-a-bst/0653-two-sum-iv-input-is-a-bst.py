# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        arr = []

        def build(root):
            if not root:
                return
    
            build(root.left)
            arr.append(root.val)
            build(root.right)

        build(root)
        
        l = 0
        r = len(arr) - 1

        while l < r:
            s = arr[l] + arr[r]
            if s == k:
                return True
            elif s < k:
                l += 1
            elif s > k:
                r -= 1
                
        return False
        