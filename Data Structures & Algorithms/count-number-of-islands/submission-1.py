class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])

        islands = 0

        def dfs(i, j):
            if i < 0 or i >= row or j < 0 or j >= col or grid[i][j] == '0':
                return
            else:
                grid[i][j] = '0'
                dfs(i+1, j)
                dfs(i-1, j)
                dfs(i, j+1)
                dfs(i, j-1)

        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    islands += 1
                    dfs(i, j)
        return islands

'''
get rows and cols, set a islands res var

Loop through each row, going column by column
 
when we  encounter a 1, we have found a valid potential island, so increment, but we need to figure out how large it is, which we need a dfs function to go through and check whether there is land above, below, left, or right of the island - call dfs on the current node

Inside of the dfs, our base case is whether the node next
to us is out of bounds top/bottom row edge - left/right col edge or if its a water block, either of these is not a valid block we can traverse onto
- the purpose of traversing onto a land block is explore
the other adjacent blocks as well as account for it

We need to recursively check up, down, left, and right
of the block we are currently on, which may lead to deeper nested calls
- Mark the visited node as 0, so that when we do perform
these deeper calls, we dont recurse back onto the same node when performing the inverse action like going from up to down then down to up - this elimates the need for a set

Once we traverse down the call stack and the original call returns, then we move onto validating the next node in our grid, the visited islands will have been marked, but its not as that matters since any future nodes would not have reached the previous islands since they would have been adjacent and found
- once you exhaust the entire grid and mark it as 0, then
you return the number of islands found
'''