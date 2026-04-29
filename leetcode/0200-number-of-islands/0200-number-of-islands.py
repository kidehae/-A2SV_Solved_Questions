class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        dir = [[0,1], [1,0], [0,-1], [-1,0]]

        res = 0

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == "0":
                return

            grid[r][c] = "0"

            for dr, dc in dir:
                n_r = r + dr
                n_c = c + dc
                dfs(n_r, n_c)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    res += 1
                    dfs(i,j)

        return res

            

      

