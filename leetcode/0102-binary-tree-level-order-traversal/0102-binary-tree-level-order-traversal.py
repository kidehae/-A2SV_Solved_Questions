class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        arr = []

        def dfs(node, level):
            if not node:
                return 
            
        
            if len(arr) == level:
                arr.append([])

            arr[level].append(node.val)

            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

    
        dfs(root, 0)
        return arr