class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        perimeter = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    for dr, dc in [(-1, 0), (1,0), (0,1), (0, -1)]:
                        nr, nc = r + dr, c + dc
                        if nr < 0 or nr == rows or nc < 0 or nc == cols or grid[nr][nc] == 0:
                            perimeter += 1
        return perimeter

'''
rows are the total number of lists in our matrix, as those are stacked

cols are the vertical columns, which is decided by the amount of elements in a single list since all lists are equal size

Loop through each list in mtx, so you need 2 for loops, one for the current row, then another going through each value in
the columns - select a row and walk through columns(idx)

If grid[r][c] == 1, that means you are visiting a valid block, so you want to check if its an internal piece, or there is
water surrounding it, only if its an edge or water surrounding it can be permiter, since an internal piece is the area

Loop through a tuple that shifts the r and c value up, down, left, right - this checks all direction, checking whether 
the shifted value at that idx is out of bounds or is a water block

In either of these cases, then we add to the perimeter, if not then we continue by shifting in a different direction until
all moves are exhausted and the perimeter is modified as fit, then we move to the next value in our current list, if it 
meets the condition of == 1, then we begin this shifting again, otherwise since we don't need to check water we continue

We dont check water because that will lead to double counting, we just need to check the land blocks, since they will
single count since we never perform the same transformation twice
'''

