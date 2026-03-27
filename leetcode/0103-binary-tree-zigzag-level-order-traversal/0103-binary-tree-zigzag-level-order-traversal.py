class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        res = []
        
        def zigzag(root, level):
            if not root:
                return
            
            if len(res) == level:
                res.append([])
            
            if level % 2 == 0:  
                res[level].append(root.val)
            else:  
                res[level].insert(0, root.val)  
            
            zigzag(root.left, level + 1)
            zigzag(root.right, level + 1)
        
        zigzag(root, 0)
        return res