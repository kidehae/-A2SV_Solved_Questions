class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        stck = deque()
        t, fresh = 0, 0

        row,col = len(grid), len(grid[0])

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    stck.append([r,c])

        dir = [[0,1], [0,-1], [1,0], [-1,0]]

        while stck and fresh > 0:
            for i in range(len(stck)):
                r, c = stck.popleft()
                for dr, dc in dir:
                    rr, cc = r + dr, c + dc
                    if rr < 0 or rr == row or cc < 0 or cc == col or grid[rr][cc] != 1:
                        continue
                    grid[rr][cc] = 2
                    stck.append([rr,cc])
                    fresh -= 1

            t += 1

        return t if fresh == 0 else -1


                
                

        