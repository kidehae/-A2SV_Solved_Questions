# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:

        self.res = 0

        def count(node):
            if not node:
                return [0,0]

            l_len,l_coin = count(node.left)
            r_len,r_coin = count(node.right)

            length = 1 + l_len + r_len
            coin = node.val + r_coin + l_coin

            self.res += abs(length - coin)

            return [length, coin]

        count(root)
        return self.res



        