class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])

        def dfs(i, j):
            if i < 0 or i >= row or j < 0 or j >= col or grid[i][j] == 0:
                return 0
            else:
                grid[i][j] = 0
                return 1 + dfs(i+1, j) + dfs(i-1, j) + dfs(i, j+1) + dfs(i, j-1)
        
        area = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    area = max(area, dfs(i,j))
        
        return area